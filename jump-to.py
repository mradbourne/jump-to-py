import json
from subprocess import check_output

config_file = open("config.json")
config = json.load(config_file)

print(config['project'])
