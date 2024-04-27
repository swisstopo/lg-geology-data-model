import mermaid as md
from mermaid.erdiagram import ERDiagram, Entity, Link

import json

import yaml

"""
{
    'zero-or-one': ['|o', 'o|'],
    'exactly-one': ['||', '||'],
    'zero-or-more': ['}o', 'o{'],
   'OneToMany': 'one-or-more'
}"""

with open("../data/geocover-schema-sde.json") as stream:
    try:
        data = json.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

graph: ERDiagram = ERDiagram("example-flowchart")

entities = {}

all_entities = []

used_entities = []

tables = data.get("tables")
for key in tables.keys():
    print(key)
    name = key.replace("TOPGIS_GC.", "")
    table = tables.get(key)

    fields = {}
    for fld in table.get("fields"):
        # print(fld)
        fields[fld.get("name")] = [fld.get("type")]
    # print(fields)
    entity = Entity(name, fields)
    entities[name] = entity
    all_entities.append(name)

fcclasses = data.get("featclasses")
for key in fcclasses.keys():
    print(key)
    name = key.replace("TOPGIS_GC.", "")
    fc = fcclasses.get(key)

    fields = {}
    for fld in fc.get("fields"):
        # print(fld)
        fields[fld.get("name")] = [fld.get("type")]
    # print(fields)
    entity = Entity(name, fields)
    entities[name] = entity
    all_entities.append(name)

"""
entity = Entity('GC_FOSSILS')
entity.add_attribute('UUID', 'uuid')

entity_1 = Entity('User', {
            'id': ['int', 'PK'],
            'name': ['string', 'the name']
        })
entity_2 = Entity('Tag', {'id': ['int', 'PK'], 'name': 'string'})
entities = [entity_1, entity_2]
"""
links = []

relationships = data.get("relationships")
for key in relationships.keys():
    relation = relationships.get(key)
    name = key.replace("TOPGIS_GC.", "")
    origin = list(map(lambda s: s.replace("TOPGIS_GC.", ""), relation.get("origin")))
    print(name, origin)
    if len(origin) != 1:
        continue
    origin = origin[0]

    destination = relation.get("destination").replace("TOPGIS_GC.", "")

    if origin in all_entities and destination in all_entities:
        print(origin, "-->", destination)
        link = Link(
            entities[origin],
            entities[destination],
            "exactly-one",
            "zero-or-more",
            dotted=True,
        )
        links.append(link)
        used_entities.append(entities[origin])
        used_entities.append(entities[destination])


diagram = ERDiagram("TOGIS - GeoCover", used_entities, links)

graphe = md.Mermaid(diagram)


graphe.to_svg("ER-GCOVER.svg")
graphe.to_png("ER-GCOVER.png")


print(diagram.script)


"""
flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]
"""
