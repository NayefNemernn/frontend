import os
import yaml

def load_config():
    with open('../config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config
config = load_config
print(f'Server IP Address: {config['ServerIPAddress']}')