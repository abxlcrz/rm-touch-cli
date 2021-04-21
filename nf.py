# Cli v1.0 
# implementation of touch command from linux in python 

import argparse
from pathlib import Path
from sys import stderr,stdout

class NfError(Exception):
    pass

def create_file(file: Path):
    dest =  Path()
    dest.cwd()
    dest= dest/file.name
    dest.touch()
    print(f'File {dest.name} created')
    

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='nf',
        description='touch command implementation in Python',
    )
    parser.add_argument(
        'name',
        type=Path,
        help='Name of the new file'
    )
    return parser.parse_args()

def main():
    args = cli()
    try:
        create_file(args.name)
    except NfError as e:
        print(e,file=stderr)
        exit(1)

if __name__=='__main__':
    main()
