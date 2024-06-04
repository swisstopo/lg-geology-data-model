import os

import arcpy
import logging


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
            self.__datasets = arcpy.ListDatasets("", "Feature")

        return self.__datasets

    @property
    def feature_classes(self):
        if len(self.__feature_classes) < 1:
            if len(self.__datasets) < 1:
                self.datasets
            logging.debug("Collecting feature classes from workspace")
            for dataset in self.__datasets:
                for fc in arcpy.ListFeatureClasses("", "All", dataset):
                    logging.debug("\n---{}---".format(fc))
                    feat_class_dict = {
                        "name": fc,
                        "type": "featclass",
                        "relationships": [],
                        "fields": [],
                        "dataset": dataset,
                    }
                    fields = arcpy.ListFields(self.__workspace + "/" + str(fc))
                    for field in fields:
                        domain = None
                        if (
                            len(field.domain) > 0
                            and field.domain in self.__coded_domains_values
                        ):
                            domain = field.domain
                        logging.debug(
                            f"    {field.name}, {field.type}, {field.length}, {domain}"
                        )

                        feat_class_dict["fields"].append(
                            dict(
                                {
                                    "name": field.name,
                                    "type": field.type,
                                    "length": field.length,
                                    "domain": domain,
                                }
                            )
                        )
                self.__feature_classes[fc] = feat_class_dict

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
            print(self.feature_classes)
            for i, fc in enumerate(self.feature_classes.keys()):
                logging.info(fc)
                desc = arcpy.Describe(fc)
                logging.info(desc)
                for j, rel in enumerate(desc.relationshipClassNames):
                    relDesc = arcpy.Describe(rel)
                    logging.debug(relDesc)

                    self.__relationships.add(rel)
        return self.__relationships
