# Cli v1.0 
# implementation of copyfile command from linux in python
 
import argparse
from pathlib import Path
from sys import stderr, stdout


class CpError(Exception):
    pass
# Enables logout data if the paramether -o is declarated

class Logger:
    def __init__(self,verbosity=False):
        self.verbose=verbosity

    def set_verbosity(self, verbosity):
        self.verbose= verbosity
    
    def log(self, message):
        if self.verbose:
            print(message)
    
    def warn(self, message, file=stdout):
        print(f'WARNING:{message}', file=file)
        
    def error(self, message, file=stderr):
        print(f'ERROR:{message}',file=file)
    

# Functions for copy

def dump(src: Path, dest: Path):
    with open(src , 'rb') as s, open(dest, 'wb') as d:
        d.write(s.read())



def copy_directory(src: Path, dest: Path, override=False):
    print('cp dir')


def copy_file(src: Path, dest: Path, override=False):
    if dest.is_dir():
        dest = dest / src.name
    if dest.is_file() and not override:
        raise CpError(f'Cannot override {dest}, specify -o option')
    print(f' Copy {src} -> {dest}')
    dest.touch()
    dump(src,dest)


def copy(src: Path, dest: Path, override=False):
    if src.is_file():
        copy_file(src, dest, override)
    elif src.is_dir():
        copy_directory(src, dest, override)
    else:
        raise CpError('File type not supported')


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='cp',
        description='cp command implementation in Python',
    )
    parser.add_argument(
        '-o','--override',
        action='store_true',
        help='override destination files if they key already exist'
    )
    parser.add_argument(
        'source',
        type=Path,
        help='Source directory or file'
    )

    parser.add_argument(
        'destination',
        type=Path,
        help='Destination directory or file'
    )

    return parser.parse_args()


def main():
    args = cli()

    # handling file types
    try:
        copy(args.source, args.destination, args.override )
    except CpError as e:
        print(e, file=stderr)
        exit(1)


if __name__ == '__main__':
    main()
