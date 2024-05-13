# Note: in Python 3.10+, this import can be removed
from __future__ import annotations

from dataclasses import dataclass, field

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

    person_dict = {'name': 'Eve', 'age': 40}
    Person = dataclass(type('Person', (object,), person_dict))
    person = Person()
    print(person)