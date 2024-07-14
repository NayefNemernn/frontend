import os
import yaml

def load_config():
    with open(os.path.join(os.path.dirname(__file__), '../full-stack/config.yaml'), 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config
config = load_config()
print(f"Server IP Address: {config['ServerIPAddress']}")
#   t e s t i n g 

 # A n o t h e r   t e s t 
