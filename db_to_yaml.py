from __future__ import annotations

# https://stackoverflow.com/questions/69773539/how-do-i-convert-a-json-file-to-a-python-class
# https://dataclass-wizard.readthedocs.io/en/latest/

import yaml
import json
from io import StringIO
from typing_extensions import TypedDict
from typing import List, Optional


class Field(TypedDict):
    name: str
    type: str
    length: int

class Table(TypedDict):
    name: str
    type: str
    relationships: str
    fields: List[Field]
    
class FeatureClass(Table):
    name: str
    type: str
    relationships: str
    fields: List[Field]
    
class Subtype(TypedDict):
    pass

class Domain(TypedDict):
    id: str
    name: str

class Relationship(TypedDict):
    origin: List[str]
    destination: str
    forwardPathLabel: str
    backwardPathLabel: str
    isAttachmentRelationship: bool
    cardinality: str
    originClassKeys: List[Key]
    destinationClassKeys: List[str]
    is_attributed: bool
    is_composite: bool
    is_reflexive: bool
    classKey: str
    keyType: str



with open("../data/geocover-schema-sde.json") as stream:
    try:
        data = json.load(stream)
    except yaml.YAMLError as exc:
         print(exc)

domain_data = data.get('domains')
#domains: dict[str, str] = domain_data
domains: Domain = domain_data

subtype_data = data.get('subtypes')
subtypes: dict[str, str] = subtype_data

table_data = data.get('tables')
tables: dict[str, Table] = table_data

feature_data = data.get('featclasses')
featclasses: dict[str, FeatureClass] = feature_data


relation_data = data.get('relationships')
relationships: dict[str, Relationship] = relation_data

'''
for idx, table in tables.items():
    print(table)
'''
    
database: dict[str, (Table, FeatureClass, Relationship, Domain)]=  data
    
ymal_string=yaml.dump(database)
print("The YAML string is:")
print(ymal_string)


