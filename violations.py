import json
import os

def load_violations(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_violations(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)