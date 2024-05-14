from anytree import AnyNode, RenderTree
import pandas as pd
import sys
import os
import logging

import logging

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)

from anytree.node.exceptions import LoopError


def reporting_anynodes(df, table_name):
    root = AnyNode(id="0", german="root", pid=None, parent=None)
    nodes = {"0": root}

    for index, row in df.iterrows():
        oid = str(int(row["GEOL_CODE_INT"]))
        pid = str(int(row["PARENT_REF"]))
        text = str(row["GERMAN"])

        node = AnyNode(id=oid, german=text, pid=pid)

        nodes[oid] = node

    for index, node in nodes.items():
        if node.pid in nodes.keys():
            parent = nodes.get(pid)
            if parent is not None:
                try:
                    node.parent = parent
                    print(node)
                    nodes[index] = node
                except LoopError as e:
                    print(f"Error: {e}")
            else:
                logging.error(f"Unknown: {node.pid}")

        else:
            logging.error(f"Oprhan: {oid}, pid={pid}", pid in nodes.keys())

            """if pid == '0':
                node = AnyNode(id=oid, german=text, pid=pid, parent=root)
                nodes[oid] = node
            else:
               parent_node = nodes.get(pid)
               if parent_node is not None:
                    node = AnyNode(id=oid, german=text, pid=pid, parent=parent_node)
                    nodes[oid] = node
               else:
                    """

    print("----")
    root = nodes.get("0")
    print(root, root.is_root)
    print(RenderTree(nodes.get("0")))


def reporting_treelib(df, table_name):
    from treelib import Node, Tree
    from treelib.exceptions import NodeIDAbsentError
    import json

    tree = Tree()
    tree.create_node("0", "0", data={"text": "Root", "pid": None})  # root node

    logging.debug(len(df))

    class NodeEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (Node, Tree)):
                return str(obj)
            # Let the base class default method raise the TypeError
            return super().default(obj)

    orphans = {}

    df = df.sort_values(["TREE_LEVEL", "GEOL_CODE_INT", "PARENT_REF"], ascending=True)

    for index, row in df.iterrows():
        oid = str(int(row["GEOL_CODE_INT"]))
        pid = str(int(row["PARENT_REF"]))
        text = str(row["GERMAN"])
        level = row["TREE_LEVEL"]
        print(oid, pid, level, text)
        data = {"pid": pid, "text": text}

        """if oid in ('15304015', ):
            print("###########################")"""
        try:
            tree.create_node(text, oid, parent=pid, data=data)

        except NodeIDAbsentError as e:
            node = Node(text, oid, data=data)
            if oid not in orphans.keys():
                orphans[oid] = node
            logging.error(f"Orphan: {oid} {text}: {e}")

    # for key in sorted(orphans.keys()):

    for key in dict(
        sorted(orphans.items(), key=lambda item: item[1].data.get("pid"))
    ).keys():
        orphan = orphans.get(key)
        pid = orphan.data.get("pid")

        node = tree.get_node(pid)

        if node:
          orphan.parent = pid
          # tree.add_node(node, parent=pid)

        del orphans[key]

    d = json.loads(tree.to_json())

    base_filepath = f"output/{table_name}"

    with open(f"{base_filepath}.json", 'w') as j:
        j.write(json.dumps(d, indent=4))

    with open(f"{base_filepath}_oprhans.json", 'w') as err:
        err.write(json.dumps(orphans, indent=4, cls=NodeEncoder))

    with open(f"{base_filepath}.csv", "w") as f:
        for id in tree.expand_tree(nid="0", mode=1, sorting=True):
            node = tree.get_node(id)
            level = tree.depth(node=id)
            spacer = "," * (int(level) - 1)
            f.write(f"{id},{node.data.get('pid')},{level},{spacer},{node.tag}\n")


def reporting(path_to_source_file, table_name):
    df = pd.read_csv(path_to_source_file, sep=",")

    df = pd.read_excel("input/export_tables.xlsx", sheet_name=table_name.upper())

    df["PARENT_REF"] = df["PARENT_REF"].fillna(0)

    logging.debug(df)

    df.sort_values(
        ["TREE_LEVEL", "GEOL_CODE_INT", "PARENT_REF"], ascending=True, inplace=True
    )

    reporting_anynodes(df, table_name)

    reporting_treelib(df, table_name)

    """print(node.ancestors)
    
    import yaml
    from anytree import AnyNode
    from anytree.exporter import DictExporter
    
    dct = DictExporter().export(root)
    print(yaml.dump(dct, default_flow_style=False))"""

    """for k,v in nodes.items():
    print(k,v)"""


def main():

    for table in ('Tecto', 'Litho', 'Litstrat', 'Chrono'):
        table_path= os.path.join('input', table + ".csv")

        reporting(table_path, table)


if __name__ == "__main__":
    main()
