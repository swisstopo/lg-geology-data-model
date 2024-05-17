import os
import pandas as pd
from treelib import Node, Tree

from treelib.exceptions import NodeIDAbsentError

import logging

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)


df = pd.read_csv("../data/TOPGIS_GC.GC_TECTO.csv", sep=",")

"""
tree = Tree()
tree.create_node("Tecto", 0)

for index, row in df.iterrows():
    code = int(row['GEOL_CODE_INT'])
    parent_id = int(row['PARENT_REF'])
    german = row['GERMAN']
    
    try:
        tree.create_node(german, code, parent=parent_id)
    except NodeIDAbsentError as e:
        print(e)

print(tree.show())"""

from bigtree import (
    Node,
    tree_to_dot,
    print_tree,
    yield_tree,
    tree_to_dict,
    tree_to_nested_dict,
)
import yaml



def reporting_using_anytree(df, table_path, table_name):
    
  # Create the root node
  root = Node("0", german="Root")

  nodes = {"0": root}

  # Assuming df is your DataFrame
  for index, row in df.iterrows():
    code = str(int(row["GEOL_CODE_INT"]))
    parent_id = str(int(row["PARENT_REF"]))
    german = row["GERMAN"]
    try:
        n = Node(code, parent=nodes[parent_id], german=german)
        nodes[code] = n
    except KeyError as e:
        logging.error(f"Orphan: {code}, {german}, parentid: {parent_id}")
    

  # Checking for orphans
  for index, row in df.iterrows():
    code = str(int(row["GEOL_CODE_INT"]))
    parent_id = str(int(row["PARENT_REF"]))
    german = row["GERMAN"]
    n = nodes.get(code)
    p = nodes.get(parent_id)
    if p is not None and n is not None:
        n.parent = p
    else:
        logging.error(f"Orphan: {code}, {german}, parentid: {parent_id}")


def reporting(df, table_path, table_name):
    logging.info(f"=== Table {table_name} ====")

    res = {'orphans': [], 'missings': []}

    # df = pd.read_csv(table_path, sep=",")
    # df["PARENT_REF"] = df["PARENT_REF"].fillna(0)

    root = Node.from_dict({"name": "0", "german": "Root"})

    nodes = {"0": root}

    for index, row in df.iterrows():
        code = int(row["GEOL_CODE_INT"])
        parent_id = int(row["PARENT_REF"])
        german = row["GERMAN"]

        n = Node.from_dict({"name": str(code), "german": german})
        nodes[str(code)] = n

    for index, row in df.iterrows():
        code = int(row["GEOL_CODE_INT"])
        parent_id = int(row["PARENT_REF"])
        german = row["GERMAN"]
        n = nodes.get(str(code))
        p = nodes.get(str(parent_id))
        if p is not None:
            n.parent = p
        else:
            logging.error(f"Orphan: {code}, {german}, parentid: {parent_id}")
            res['orphans'].append(int(code))
            res['missings'].append(int(parent_id))

    return res

    # print_tree(root, attr_list=["german"])

    """
  d =tree_to_nested_dict(root, name_key="geol_code_int", all_attrs=True)


  with open(f'output/bigtree_{table_name.lower()}.yaml', 'w') as f:
    documents = yaml.dump(d, f)


  with open(f"output/bigtree_{table_name.loser()}.csv", "w") as f:

    for branch, stem, node in yield_tree(root, style="ascii"):
        #parents = "/".join(list(node.ancestors))
        
        parents = "/".join([n.node_name for n in node.ancestors])
        
        
        print(f"{branch},{stem},{node.german},{parents}\n")"""


def get_df(table_name):
    df = pd.read_excel("input/export_tables.xlsx", sheet_name=table_name.upper())

    df["PARENT_REF"] = df["PARENT_REF"].fillna(0)
    df["REMARK"] = ""

    return df


def main():
    with pd.ExcelWriter('input/alain.xlsx') as writer:

      for table_name in ("Tecto", "Litho", "Litstrat", "Chrono"):
        table_path = os.path.join("input", table_name + ".csv")

        df = get_df(table_name)

        result = reporting(df, table_path, table_name)

        orphans = result.get('orphans')

        if orphans is not None:

            df['REMARK'] = df['GEOL_CODE_INT'].apply(lambda x: 'orphan' if int(x) in orphans else '')

        df.to_excel(writer, sheet_name=table_name.upper())


        # reporting_using_anytree(df, table_path, table_name)


if __name__ == "__main__":
    main()
