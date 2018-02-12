import subprocess
import os

def cmd(command):
    return subprocess.check_output(command, universal_newlines=True).strip()

def open_in_default_editor(filepath):
    cmd(['open', filepath])
