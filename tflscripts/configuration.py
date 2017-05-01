import os
import json

def read_configuration():
    path = os.path.dirname(os.path.realpath(__file__))
    with open(path + '/configuration.json') as f:
        config = json.load(f)
    return config
