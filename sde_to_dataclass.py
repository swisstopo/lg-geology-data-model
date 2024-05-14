# Note: in Python 3.10+, this import can be removed
from __future__ import annotations

from dataclasses import dataclass, field

from dataclasses import asdict, make_dataclass
from typing import Optional, List, Union, Dict, Any, NamedTuple, DefaultDict, Literal


from dataclass_wizard import JSONWizard
import json

from typing import Dict

@dataclass
class CodedDomain:
    codes: Dict[int, str]



@dataclass
class MyClass(JSONWizard):
    my_str: str | None
    is_active_tuple: tuple[bool, ...]
    list_of_int: list[int] = field(default_factory=list)

@dataclass
class Field(JSONWizard):
    name: str
    type: str
    length: int

@dataclass
class Table(JSONWizard):
    name: str
    type: str
    relationships: list
    fields: list[Field]

@dataclass
class Field(JSONWizard):
    name: str
    type: str
    length: int

@dataclass
class Key(JSONWizard):
    name: str
    role: str
@dataclass
class Relationship(JSONWizard):
    origin: list
    destination: str
    forwardPathLabel: str
    backwardPathLabel: str
    isAttachmentRelationship: bool
    cardinality: Literal['OneToMany', 'ManyToMany']
    originClassKeys: list[Key]
    destinationClassKeys: list[Key]
    is_attributed: bool
    is_composite: bool
    is_reflexive: bool
    classKey: str
    keyType: str



with open(r"../data/geocover-schema-sde.json") as f:
    data = json.load(f)

# De-serialize the JSON string into a `MyClass` object.

tables = data.get('tables')
for name in tables:
    t = tables.get(name)

    table = Table.from_dict(t)
    print(table)

domains = data.get('domains')
for name in domains:
    d = domains.get(name)

    domain = CodedDomain(d)
    print(domain)

    '''
    Impossible as  '1' is not a valid variable name
    CD = make_dataclass('CodedDomain',  list(d.items()))
    x = CD(**d)

    print(asdict(x))
    # {'i': 42, 's': 'text'}
    '''
relationships = data.get('relationships')
for name in relationships:
    t = relationships.get(name)

    relationship = Relationship.from_dict(t)
    print(relationship)
