from src.utils import cmd

origin_url = cmd(['git', 'config', '--local', 'remote.origin.url'])

def git():
    print('jumping to github repo')

def branch():
    print('jumping to branch')

def pr():
    # Creates or opens PR on GitHub
    print('jumping to existing pr or create pr page')
