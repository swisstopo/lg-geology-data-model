import os
import json

import arcpy
import logging

from collections import OrderedDict


from utils import merge_two_dicts, get_field_type

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)


EXCLUDE_TABLES = [
    "TOPGIS_GC.GC_EXPLOIT_GEOMAT_PLG",
    "TOPGIS_GC.GC_LINEAR_OBJECTS",
    "TOPGIS_GC.GC_POINT_OBJECTS",
    "TOPGIS_GC.GC_FOSSILS",
    "TOPGIS_GC.GC_UNCO_DESPOSIT",
    "TOPGIS_GC.GC_BEDROCK",
    "TOPGIS_GC.GC_SURFACES",
]


remove_prefix = lambda x: x.split(".")[-1]

gc_filter = lambda x: "GC_" in x and not x.endswith("_I") and x not in EXCLUDE_TABLES


class GeocoverSchema:
    __instance = None

    @staticmethod
    def instance(workspace):
        """Static access method."""
        if GeocoverSchema.__instance is None:
            GeocoverSchema(workspace)

        return GeocoverSchema.__instance

    def __repr__(self):
        return f"<GeocoverSchema {self.__workspace}>"

    def __init__(self, workspace):
        """Virtually private constructor."""
        if GeocoverSchema.__instance is not None:
            raise Exception("Forbidden access to singleton class")
        else:
            GeocoverSchema.__instance = self
            arcpy.env.workspace = self.__workspace = workspace

            self.__tables = []
            self.__coded_domains = []
            self.__coded_domains_values = {}
            self.__datasets = []
            self.__feature_classes = {}
            self.__feature_class_subtypes = {}
            self.__geol_code = {}
            self.__relationships = set()
            self.__connection_info = None
            self.__feature_classes_list = []
            self.__esri_style_dump  = True

    def generate_filter_function():
        def filter_function(name):
            return (
                not name.endswith("_I")
                and name.startswith("GC_")
                and name not in EXCLUDE_TABLES
            )

        return filter_function

    @property
    def connection_info(self):
        if self.__connection_info is None:
            desc = arcpy.Describe(self.__workspace)
            cp = desc.connectionProperties

            connection_info = {
                "workspace": {
                    "ConnectionString": desc.connectionString,
                    "WorkspaceFactoryProgID": desc.workspaceFactoryProgID,
                    "WorkspaceType:": desc.workspaceType,
                },
                "connection": {
                    "Server": cp.server,
                    "Instance": cp.instance,
                    "Version": cp.version,
                },
            }

            self.__connection_info = connection_info

        return self.__connection_info

    @property
    def tables(self):
        if len(self.__tables) < 1:
            logging.debug("Collecting tables from workspace")
            self.__tables = [table.split(".")[-1] for table in arcpy.ListTables()]

        return self.__tables

    def list_coded_domains(self):
        if len(self.__coded_domains) < 1:
            gc_filter = lambda x: "GC_" in x.name
            logging.debug("Collecting coded domains from workspace")
            coded_domains_list = arcpy.da.ListDomains(self.__workspace)
            self.__coded_domains = list(filter(gc_filter, coded_domains_list))

        return self.__coded_domains

    @property
    def coded_domains(self):
        if len(self.list_coded_domains()) < 1:
            self.list_coded_domains()
        for domain in self.list_coded_domains():
            if not self.__esri_style_dump:
                if domain.domainType == "CodedValue":
                    coded_values = domain.codedValues
                    domain_dict = {}
                    for val, desc in coded_values.items():
                        domain_dict[val] = desc
            else:
                domain_dict = {"type": domain.domainType, "codedValues": domain.codedValues}

            self.__coded_domains_values[domain.name] = domain_dict

        return self.__coded_domains_values

    @property
    def datasets(self):
        if len(self.__datasets) < 1:
            logging.debug("Collecting datasets from workspace")
            self.__datasets = arcpy.ListDatasets()

        return self.__datasets

    def fields(self, feature_class_name):
        fields_list = []
        fields = arcpy.ListFields(feature_class_name)

        for field in fields:
            domain = None
            if len(field.domain) > 0 and field.domain in self.__coded_domains_values:
                domain = field.domain
            logging.debug(f"    {field.name}, {field.type}, {field.length}, {domain}")

            fields_list.append(
                dict(
                    {
                        "name": field.name,
                        "type": field.type,
                        "length": field.length,
                        "domain": domain,
                    }
                )
            )
        return fields_list

    @property
    def feature_classes_list(self):
        if len(self.__feature_classes_list) < 1:
            logging.debug("Collecting feature classes list from workspace")
            feature_classes_list = []
            walk = arcpy.da.Walk(datatype="FeatureClass")
            for root, dataset, fcs in walk:
                for fc in fcs:
                    feature_classes_list.append(fc)
            self.__feature_classes_list = list(filter(gc_filter, feature_classes_list))

            logging.info(f"Filtered list: {self.__feature_classes_list}")

        return self.__feature_classes_list

    @property
    def feature_classes(self):
        if len(self.__feature_classes) < 1:
            if len(self.__feature_classes_list) < 1:
                self.feature_classes_list
            logging.debug("Collecting feature classes from workspace")

            for fc in self.__feature_classes_list:
                logging.debug("--- Feature class: {} ---".format(fc))
                feat_class_dict = {
                    "name": fc,
                    "type": "featclass",
                    "relationships": [],
                    "fields": [],
                }

                self.__feature_classes[fc] = self.fields(fc)

        return self.__feature_classes

    @property
    def tables(self):
        if len(self.__tables) < 1:
            logging.debug("Collecting tables from workspace")
            self.__tables = list(map(remove_prefix, arcpy.ListTables()))

        return self.__tables

    @property
    def relationships(self):
        if len(self.__relationships) < 1:
            logging.debug("Collecting relationships from workspace")
            logging.debug(self.feature_classes)
            for i, fc in enumerate(self.feature_classes.keys()):
                desc = arcpy.Describe(fc)
                logging.debug(desc)
                for j, rel in enumerate(desc.relationshipClassNames):
                    relDesc = arcpy.Describe(rel)
                    logging.debug(relDesc)

                    self.__relationships.add(rel)
        return self.__relationships

    @property
    def subtypes(self, expand=False):
        if len(self.__feature_class_subtypes) < 1:
            logging.debug("Collecting relationships from workspace")
            subtypes_layers_dict = {}
            subtypes_dict = {}
            walk = arcpy.da.Walk(datatype="FeatureClass")
            list_subtypes = lambda x: arcpy.da.ListSubtypes(x).items()

            for fc in self.feature_classes.keys():
                try:
                    subtypes = arcpy.da.ListSubtypes(os.path.join(self.__workspace, fc))
                except OSError as e:
                    logging.error(e)
                    continue
                d = []
                desc_lu = {key: value["Name"] for (key, value) in subtypes.items()}
                subtypes_dict = merge_two_dicts(subtypes_dict, desc_lu)

                for stcode, stdict in list(subtypes.items()):
                    logging.debug({stcode: stdict["Name"]})
                    logging.debug(f"  Subtype Code: {stcode}")
                    logging.debug(f"  Subtype Name: {stdict['Name']}")
                    logging.debug(f"  Subtype Field:{stdict['SubtypeField']}")
                    logging.debug(f"  Subtype Default:{stdict['Default']}")

                    d.append({stcode: stdict})

                    field_type_dict = get_field_type(stdict)

                subtypes_layers_dict[fc] = d

            if expand:
                self.__feature_class_subtypes = subtypes_layers_dict
            else:
                self.__feature_class_subtypes = OrderedDict(
                    sorted(subtypes_dict.items())
                )

            return self.__feature_class_subtypes
