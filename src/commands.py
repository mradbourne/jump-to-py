from src import config
from src.modules import git

def run_command(command, args):
    if command == 'init':
        config.init_config()

    if command == 'configs':
        config.open_config_dir()

    if command == 'config':
        config.open_config()

    if command == 'args':
        print(args)

    if command == 'rm':
        config.remove_config()
