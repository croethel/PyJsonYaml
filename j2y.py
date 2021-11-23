# Write a simple python script:
# j2y.py - a json to yaml converter
# then translate both jason files to yaml files

import json
import yaml
import os

def json_to_yaml(file_path: str):
    with open(file_path, 'r') as f:
        output_file = open(os.path.basename(file_path).replace(".json","")+'.yaml', 'w')
        output_file_content = {}
        output_file_content = json.load(f)
        yaml.dump(output_file_content, output_file)
        output_file.close()


# json_to_yaml('donuts.json')
# json_to_yaml('emojis.json')

json_to_yaml('verify_test.json')