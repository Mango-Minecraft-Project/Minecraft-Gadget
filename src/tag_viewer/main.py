import json
import os

"""
${folder_name}/${namespace}/tags/${'items'|'blocks'|'fluids'}/...
"""

data_path = "./data/tag_viewer/"

tag_collection = {"items": {}, "blocks": {}, "fluids": {}}

for root, dirs, files in os.walk(data_path):
    root = root[len(data_path) :].replace("\\", "/").split("/")
    if len(root) > 4 and root[-2] == 'tags':
        print(root, dirs, files)
