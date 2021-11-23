# Write a simple python script:
# y2j.py - a yaml to json converter
# then translate both yaml files to json files

import json
import yaml
import os

def yaml_to_json(file_path: str):
    with open(file_path, 'r') as f:
        output_file = open(os.path.basename(file_path).replace(".yaml","")+'.json', 'w')
        output_file_content = yaml.load(f, Loader=yaml.FullLoader)
        json.dump(output_file_content, output_file)
        output_file.close()


yaml_to_json('verify.yaml')
yaml_to_json('xmas.yaml')

yaml_to_json('donuts_test.yaml')