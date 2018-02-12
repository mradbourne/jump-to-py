import argparse

def get_args():
    arg_parser = argparse.ArgumentParser(description='Process some integers.')
    arg_parser.add_argument('command', metavar='N', type=str, nargs='+',
        help='help here')
    arg_parser.add_argument('--sum', dest='accumulate', action='store_const',
        const=sum, default=max,
        help='sum the integers (default: find the max)')
    return arg_parser.parse_args()
