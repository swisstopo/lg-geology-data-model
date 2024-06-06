import os

import arcpy
import logging

from collections import OrderedDict


from utils import merge_two_dicts, get_field_type

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)


EXCLUDE_TABLES = [
    "GC_REVISIONSEBENE",
    "GC_CONFLICT_",
    "GC_ERRORS_",
    "GC_VERSION",
    "GC_MAPSHEET",
]


remove_prefix = lambda x: x.split(".")[-1]

gc_filter = lambda x: "GC_" in x or not x.endswith("_I")


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

    @property
    def tables(self):
        if len(self.__tables) < 1:
            logging.debug("Collecting tables from workspace")
            self.__tables = [table.split(".")[-1] for table in arcpy.ListTables()]

        return self.__tables

    def list_coded_domains(self):
        if len(self.__coded_domains) < 1:
            logging.debug("Collecting coded domains from workspace")
            self.__coded_domains = arcpy.da.ListDomains(self.__workspace)

        return self.__coded_domains

    @property
    def coded_domains(self):
        if len(self.list_coded_domains()) < 1:
            self.list_coded_domains()
        for domain in self.list_coded_domains():
            if domain.domainType == "CodedValue":
                coded_values = domain.codedValues
                domain_dict = {}
                for val, desc in coded_values.items():
                    domain_dict[val] = desc
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
    def feature_classes(self):
        if len(self.__feature_classes) < 1:
            if len(self.__datasets) < 1:
                self.datasets
            logging.debug("Collecting feature classes from workspace")
            walk = arcpy.da.Walk(datatype="FeatureClass")
            for root, dataset, fcs in walk:
                for fc in fcs:
                    logging.info("--- Feature class: {} ---".format(fc))
                    feat_class_dict = {
                        "name": fc,
                        "type": "featclass",
                        "relationships": [],
                        "fields": [],
                        "dataset": dataset,
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
                logging.info(fc)
                desc = arcpy.Describe(fc)
                logging.info(desc)
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
