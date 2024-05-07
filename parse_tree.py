from anytree import AnyNode, RenderTree
import pandas as pd
import sys

from anytree.node.exceptions import LoopError

path_to_source_file = r'input/Tecto.csv'

root = AnyNode(id="0", german='root', pid=None, parent=None)
nodes = {'0': root}

df=  pd.read_csv(path_to_source_file, sep=",")


df = pd.read_excel('input/export_tables.xlsx', sheet_name='TECTO')


df['PARENT_REF'] = df['PARENT_REF'].fillna(0)

print(df)

df.sort_values(by=['GEOL_CODE_INT', 'PARENT_REF', 'TREE_LEVEL'], inplace=True)


for index, row in df.iterrows():
            oid = str(int(row['GEOL_CODE_INT']))
            pid = str(int(row['PARENT_REF']))
            text = str(row['GERMAN'])

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
                print(f"Unknown: {node.pid}")

        else:
            print(f"Oprhan: {oid}, pid={pid}", pid in nodes.keys())

            '''if pid == '0':
                node = AnyNode(id=oid, german=text, pid=pid, parent=root)
                nodes[oid] = node
            else:
               parent_node = nodes.get(pid)
               if parent_node is not None:
                    node = AnyNode(id=oid, german=text, pid=pid, parent=parent_node)
                    nodes[oid] = node
               else:
                    '''



print('----')
root = nodes.get('0')
print(root, root.is_root)
print(RenderTree(nodes.get('0')))

sys.exit()

from treelib import Node, Tree
from treelib.exceptions import NodeIDAbsentError
import json

tree = Tree()
tree.create_node("0", "0")  # root node

print(len(df))


orphans ={}

for index, row in df.iterrows():
            oid = str(int(row['GEOL_CODE_INT']))
            pid = str(int(row['PARENT_REF']))
            text = str(row['GERMAN'])
            try:
                tree.create_node(text, oid, parent=pid)
                if pid =='15303100':
                    print('####')

            except NodeIDAbsentError as e:
                node = Node(text, oid, data={'pid': pid})
                if oid not in orphans.keys():
                    orphans[oid] = node
                print(f"Orphan: {oid}: {e}")

for key in sorted(orphans.keys()):
    orphan =orphans.get(key)
    pid = orphan.data.get('pid')
    node = orphans.get(pid)

    if node:
        tree.add_node(node, parent=pid)

        print(node)

d = json.loads(tree.to_json())

#print(json.dumps(d, indent=4))



'''print(node.ancestors)

import yaml
from anytree import AnyNode
from anytree.exporter import DictExporter

dct = DictExporter().export(root)
print(yaml.dump(dct, default_flow_style=False))'''

'''for k,v in nodes.items():
    print(k,v)'''



