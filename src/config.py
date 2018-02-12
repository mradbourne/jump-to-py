import os
import json
from pathlib import Path
import urllib.parse
from src.utils import cmd, open_in_default_editor

current_dir = os.getcwd()
home_dir = os.getenv('HOME')
config_dir = '/.jump-to/configs/'
config_dir_path = home_dir + config_dir
config_name = urllib.parse.quote_plus(current_dir) + '.json'
config_path = config_dir_path + config_name


def open_config_dir():
    the_path = Path(config_dir_path)
    if the_path.is_dir():
        cmd(['open', config_dir_path])
    else:
        home_path = Path(home_dir)
        if home_path.is_dir():
            cmd(['mkdir', config_dir])
        else:
            print('Can\'t find your home directory')

def open_config():
    the_path = Path(config_path)
    if the_path.is_file():
        open_in_default_editor(config_path)
    else:
        print('Config does not exist')

def remove_config():
    # TODO: Warn first
    print('Removing config...')
    cmd(['rm', config_path])

def init_config():
    print('Initializing config...')
    file = open(config_path, 'w') 
    file.write('{\n')
    file.write('  "project": "coolProject"\n')
    file.write('}\n')
    file.close() 

def get_config():
    the_path = Path(config_path)
    if the_path.is_file():
        config_file = open(config_path)
        return json.load(config_file)
    else:
        return None
