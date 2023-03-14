import json
import os

"""
${folder_name}/${namespace}/tags/${'items'|'blocks'|'fluids'}/...
"""

data_path = "./data/tag_viewer/"

tag_collection = {"items": {}, "blocks": {}, "fluids": {}}

for root, dirs, files in os.walk(data_path):
    root = root[len(data_path) :].replace("\\", "/")
    root_ = root.split("/")
    if not dirs and len(root_) > 4 and (root_[i:=-2] == 'tags' or root_[i:=-3] == 'tags'):
        namespace, type = root_[i-1], root_[i+1]
        for file in files:
            tag_name = f"{namespace}:{f'{root_[-2]}/' if i == -3 else ''}{root[-1]}"
            with open(f'{root}/{file}') as file:
                _data = json.load(file)
            tag_collection[type][namespace] = tag_collection[type].get(tag_name, {}) | ...
        print(root, files, sep='\n', end='\n\n')