import json
import subprocess

def c(cmd):
    return subprocess.check_output(cmd, universal_newlines=True).strip()

def init():
    config_file = open("config.json")
    config = json.load(config_file)

origin_url=c(["git", "config", "--local", "remote.origin.url"])
print(origin_url)
