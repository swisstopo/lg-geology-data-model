import json
import logging
import os
import sys
from collections import OrderedDict

import arcpy

from utils import arcgis_table_to_df, get_field_type, merge_two_dicts

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)


EXCLUDE_TABLES = [
    "TOPGIS_GC.GC_REVISIONSEBENE",
    "TOPGIS_GC.GC_CONFLICT_POLYGON",
    "TOPGIS_GC.GC_MAPSHEET",
    "TOPGIS_GC.GC_ERRORS_POLYGON",
    "TOPGIS_GC.GC_ERRORS_MULTIPOINT",
    "TOPGIS_GC.GC_ERRORS_LINE",
]

TREE_TABLES = [
    "TOPGIS_GC.GC_LITHO",
    "TOPGIS_GC.GC_LITSTRAT",
    "TOPGIS_GC.GC_CHRONO",
    "TOPGIS_GC.GC_TECTO",
    "TOPGIS_GC.GC_ADMIXTURE",  # Not a hierarchical table
]

TREE_TABLE_FIELD = list(
    (
        "OBJECTID",
        "GEOL_CODE",
        "GEOL_CODE_INT",
        "GERMAN",
        "FMAT_LITSTRAT",
        "GERMAN",
        "TREE_LEVEL",
        "PARENT_REF",
    )
)


remove_prefix = lambda x: x.split(".")[-1]

gc_filter = lambda x: "GC_" in x and not x.endswith("_I") and x not in EXCLUDE_TABLES

table_filter = lambda x: x in TREE_TABLES


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

            self.__tables = {}
            self.__tables_list = []
            self.__coded_domains = []
            self.__coded_domains_values = {}
            self.__datasets = []
            self.__feature_classes = {}
            self.__feature_class_subtypes = {}
            self.__geol_code = {}
            self.__relationships = {}
            self.__connection_info = None
            self.__feature_classes_list = []
            self.__esri_style_dump = True

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
    def tables_list(self):
        if len(self.__tables_list) < 1:
            logging.debug("Collecting tables from workspace")
            self.__tables_list = list(filter(gc_filter, arcpy.ListTables()))

        return self.__tables_list

    @property
    def tables(self):
        tables = {}
        if len(self.__tables_list) < 1:
            self.tables_list

        for table_name in self.__tables_list:
            logging.info(table_name)

            self.__tables[table_name] = self.fields(table_name)

        return self.__tables

    @property
    def tree_tables(self):
        tables = {}
        if len(self.__tables_list) < 1:
            self.tables_list

        if len(self.__coded_domains_values) < 1:
            self.coded_domains

        for table_name in list(filter(table_filter, self.__tables_list)):
            logging.info(table_name)

            try:
                df = arcgis_table_to_df(table_name, input_fields=TREE_TABLE_FIELD)
                self.__tables[table_name] = df
            except KeyError as e:
                logging.error(f"Table {table_name} has nokey: {e}")
                continue

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
        if len(self.__coded_domains_values) < 1:
            for domain in self.list_coded_domains():
                if not self.__esri_style_dump:
                    if domain.domainType == "CodedValue":
                        coded_values = domain.codedValues
                        domain_dict = {}
                        for val, desc in coded_values.items():
                            domain_dict[val] = desc
                else:
                    domain_dict = {
                        "type": domain.domainType,
                        "codedValues": domain.codedValues,
                    }

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

        if len(self.__coded_domains_values) < 1:
            self.coded_domains

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
    def relationships(self):
        if len(self.__relationships) < 1:
            logging.debug("Collecting relationships from workspace")

            for i, fc in enumerate(self.feature_classes_list):
                desc = arcpy.Describe(fc)

                for j, rel in enumerate(desc.relationshipClassNames):
                    relDesc = arcpy.Describe(rel)
                    r_name = str(fc).replace("/", "-")

                    self.__relationships[r_name] = relDesc
        return self.__relationships

    @property
    def subtypes(self, expand=False):
        if len(self.__feature_class_subtypes) < 1:
            logging.debug("Collecting relationships from workspace")
            if len(self.__feature_classes_list) < 1:
                self.feature_classes_list
            subtypes_layers_dict = {}
            subtypes_dict = {}

            list_subtypes = lambda x: arcpy.da.ListSubtypes(x).items()

            for fc in self.__feature_classes_list:
                logging.debug(f"-----{fc} ------")
                try:
                    subtypes = arcpy.da.ListSubtypes(fc)
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
