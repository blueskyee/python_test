import yaml

def parse_config(yaml_file_path=None):
    with open(yaml_file_path, 'r') as f:
        try:
            doc = yaml.load(f)
        except yaml.YAMLError as e:
            print(e)
    return doc


def parse_keys_values(config):
    for key, value in config.iteritems():
        print('key: {}, value: {}'.format(key, value))


def parse_schema(config):
    for key, value in config['schema'].iteritems():
        print('key: {}, value: {}'.format(key, value))


def parse_data_subject(config):
    return config['data_subject']

def parse_partition(config):
    return ','.join(str(e) for e in config['partition'])

def parse_input_path(config):
    return config['input_path']

def parse_output_path(config):
    return config['output_path']

def parse_streaming_host(config):
    return config['streaming']['host']

def parse_streaming_topic(config):
    return config['streaming']['topic']


