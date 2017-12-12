import yaml

def parse_config(yaml_file_path=None):
    with open(yaml_file_path, 'r') as f:
	try:
	    doc = yaml.load(f)
	except yaml.YAMLError as e:
            print(e)
    return doc

