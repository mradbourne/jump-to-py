from src.config import get_config
from src.args import get_args
from src.commands import run_command

if __name__ == '__main__':
    config = get_config()
    print('---')
    print(config)
    print('---')

    args = get_args()
    run_command(command=args.command[0], args=args)
