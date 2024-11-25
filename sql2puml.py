# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <martin.groenholdt@gmail.com> wrote this file. As long as you retain this notice
# you can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Martin B. K. Grønholdt
# --------------------------------------------------------------------------------

"""
Name: sql2puml..py
Author: Martin Bo Kristensen Grønholdt.
https://github.com/deadbok/py-puml-tools/blob/master/dbsql2puml/sql2puml.py

Parse SQL tables into a Plant UML databse diagram.

table(countryTable) {
	primary_key(idCountry) INTEGER
	---
	country TEXT
}

table(cityTable) {
	primary_key(idCity) INTEGER
	foreign_key(country,countryTable.idCountry) TEXT
	---
	city TEXT
}
"""
#from sqlparsetables import SQLParseTables
from collections import OrderedDict

DEFAULT_TEMPLATE = """
@startuml

skinparam monochrome true
skinparam linetype ortho
scale 2

!define table(x) class x << (T,#FFAAAA) >> #FFF
!define view(x) class x << (V,#FFAAAA) >>
!define ent(x) class x << (E,#FFAAAA) >>
!define enum(x) class x << (E,#FFAAAA) >>
!define class(x) class x << (C, #CC8888) >> #EEEBDC

!define primary_key(x) <b>PK: x</b>
!define foreign_key(x,reference) <b>FK: </b>x
!define key(x) <b>x</b>
hide methods
hide stereotypes

{}
@enduml
"""

class NoTableException(ValueError):
    """
    Exception raised when trying to add a column without first adding a table.
    """
    pass


class SQL2PUML:
    """
    Parse SQL and convert CREATE TABLE statements to a Plant UML database graph.
    """

    def __init__(self, puml_template=None, template_file=None):
        """
        Initialize the SQL2PUML parser.

        :param puml_template: A custom Plant UML template string.
        :param template_file: A filename containing the Plant UML template.
        """
        if puml_template and template_file:
            raise ValueError("Specify either 'puml_template' or 'template_file', not both.")
        
        # Load template from a string or a file
        if puml_template:
            self.puml_template = puml_template
        elif template_file:
            with open(template_file, 'r', encoding='utf-8') as f:
                self.puml_template = f.read()
        else:
            # Default template
            self.puml_template = DEFAULT_TEMPLATE

        # Data structures for parsed SQL
        self.puml_tables = OrderedDict()
        self.puml_enumerations = OrderedDict()
        self.current_table = None

    # Template structure when the SQL is parsed.
    puml_enumerations = OrderedDict()

    def add_enum(self, name, enum):
        """
        Add an enumeration to the PUML structure.

        :param name: Name of the enumeration.
        """
        self.puml_enumerations[name] = enum

    def add_table(self, name):
        """
        Add a table to the PUML structure.

        :param name: Name of the table.
        """
        self.puml_tables[name] = {
            'default': OrderedDict(),
            'foreign': OrderedDict(),
            'primary': OrderedDict()
        }
        # Set current table name.
        self.current_table = name

    def add_column(self, name, type):
        """
        Add a column to a table in the PUML structure.

        :param name: Name of the column.
        :param type: Type of the column.
        """

        # Refuse if not in a table
        if self.current_table is None:
            raise NoTableException

        self.puml_tables[self.current_table]['default'][name] = type

        if name.lower() == 'shape' and type.lower().strip() == 'geometry':
            self.puml_tables[self.current_table]['is_feature_class'] = True



    def add_column_primary(self, name, type):
        """
        Add a primary key to a table in the PUML structure.

        :param name: Name of the primary key.
        :param type: Type of the primary key.
        """
        # Refuse if not in a table
        if self.current_table is None:
            raise NoTableException

        self.puml_tables[self.current_table]['primary'][name] = type

    def add_column_foreign(self, name, type, reference):
        """
        Add a foreign key to a table in the PUML structure.

        :param name: Name of the foreign key.
        :param type: Type of the foreign key.
        :param reference: Foreign key reference.
        """
        # Refuse if not in a table
        if self.current_table is None:
            raise NoTableException

        self.puml_tables[self.current_table]['foreign'][name] = (type, reference)

    def clear(self):
        """
        Clear the variabes used while generating the Plant UML output.
        """
        self.puml_tables = OrderedDict()
        self.current_table = None

    def transform(self, sql=None, enum=False):
        """
        Transform SQL CREATE TABLE statements to a Plant UML database graph.

        :param sql: SQL file.
        :return: PUML document string.
        """
        # Start from scratch.
        #self.clear()
        # Parse the SQL into the internal structure.
        #self.parse(sql)

        # Create an empty list of linus in the output.
        puml_lines = list()
        # Run through all tables.
        for table_name, table in self.puml_tables.items():
            # Add PUML code for the beggining of the table.
            class_name = 'table'
            if table.get('is_feature_class'):
                class_name = 'class'
            puml_lines.append('{}({}) '.format(class_name, table_name) + '{')

            # Add PUML lines for all primary keys.
            for cname, ctype  in table['primary'].items():
                 puml_lines.append('\tprimary_key({}) {}'.format(cname, ctype))

            # Add PUML lines for all foreign keys.
            for cname, cval  in table['foreign'].items():
                puml_lines.append('\tforeign_key({},{}) {}'.format(cname, cval[1], cval[0]))

            # Add separator if there is regular columns.
            if len(table['default'].keys()) > 0:
                puml_lines.append('\t---')

            # Add regular columns.
            # Sort keys except OBJECTID and UUID
            keys = list(table['default'].keys())
            if len(keys) > 1 and keys[0].lower() == 'objectid' and keys[1].lower() == 'uuid':
                keys = keys[:2] + sorted(keys[2:])
            sorted_keys = {i: table['default'][i] for i in keys}
            for cname, ctype  in sorted_keys.items():
                puml_lines.append('\tkey({}) {}'.format(cname, ctype))

            # Close the table.
            puml_lines.append('}')
            # Add a single empty line.
            puml_lines.append('')

        # Run through all foreign keys and crete the table relations.
        for table_name, table in self.puml_tables.items():
            for fk  in table['foreign'].values():
                foreign_table = fk[1].split('.')[0]
                if foreign_table != table_name:
                    puml_lines.append('{} "0..n" -- "1..1" {}'.format(table_name, foreign_table))
        puml_lines.append('')

        # Add the puml_enumerations
        if enum:
          for enum_name, enum in self.puml_enumerations.items():
            # Add PUML code for the beggining of the enum.
            puml_lines.append('enum({}) '.format(enum_name) + '{')
            # Add PUML lines for all primary keys.
            for cname, ctype  in enum.items():
                 puml_lines.append('\tkey({}) {}'.format(cname, ctype))
            # Close the enum.
            puml_lines.append('}')
            # Add a single empty line.
            puml_lines.append('')

          # Add a single empty line.
          puml_lines.append('')

        # Join all output lines separated by new lines.
        content = '\n'.join(puml_lines)

        # Return the final PUML string.
        return (self.puml_template.format(content=content))
