import json

def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config

config = load_config()
MODEL = config['model']
CTXLENGTH = config['contextlength']
CONSTANTCONTEXT = config['constantcontext']
DELIMITER = config['delimiter']
DOCFOLDER = config['docfolder']