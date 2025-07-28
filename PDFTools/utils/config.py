import json
import os

def load_config():
    try:
        if os.path.exists('config.json'):
            with open('config.json', 'r') as f:
                return json.load(f)
        return {'theme': 'light', 'primary_color': '#00CED1'}
    except Exception:
        return {'theme': 'light', 'primary_color': '#00CED1'}

def save_config(config):
    try:
        with open('config.json', 'w') as f:
            json.dump(config, f)
    except Exception:
        pass