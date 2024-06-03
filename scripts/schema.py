
import os

import arcpy
import logging



logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)

class GeocoverSchema:
     __instance = None

     @staticmethod
     def instance(workspace):
         """ Static access method. """
         if GeocoverSchema.__instance is None:
             GeocoverSchema(workspace)

         return GeocoverSchema.__instance

     def __repr__(self):
         return f"<GeocoverSchema {self.__workspace}>"


     def __init__(self, workspace):
         """ Virtually private constructor. """
         if GeocoverSchema.__instance is not None:
             raise Exception("Forbidden access to singleton class")
         else:
             GeocoverSchema.__instance = self
             arcpy.env.workspace = self.__workspace = workspace

             self.__tables = []
             self.__coded_domains = []
             self.__datasets = []
             self.__feature_classes = {}
             self.__feature_class_subtypes = {}
             self.__geol_code = {}

     @property
     def tables(self):

        if len(self.__tables) < 1:
            logging.debug("Collecting tables from workspace")
            self.__tables = [table.split('.')[-1] for table in arcpy.ListTables()]

        return self.__tables

     @property
     def domains(self):
         if len(self.__coded_domains) < 1:
             logging.debug("Collecting coded domains from workspace")
             self.__coded_domains = arcpy.da.ListDomains(self.__workspace)

         return self.__coded_domains




