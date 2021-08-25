#!/usr/bin/python3

from src.rebuild_deb import rebuild_deb, printout
import argparse
import sys
import os


def get_arguments():
    parser = argparse.ArgumentParser(description='Inject bash scripts in debian packages.', usage=f'{sys.argv[0]} -d debian_package -b bash_file', epilog=f'EXAMPLE - {sys.argv[0]} -d /tmp/file.deb -b /tmp/script.sh')
    parser.add_argument('-v', '--version', action='version', version='1.0')
    parser.add_argument(
        '-d', dest='deb', metavar='debian package', help='target debian package')
    parser.add_argument('-b', dest='bash', metavar='bash script',
                        help='bash script containing payload')
    args = parser.parse_args()
    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)
    return args


def read_content(script: str):
    file = open(script, 'r')
    content = file.read()
    file.close()
    return content


args = get_arguments()

deb = args.deb
bash = args.bash

if not os.path.exists(deb) or not os.path.exists(bash):
    printout('[+] File Does Not Exists', 'red', True)
    sys.exit()

payload = read_content(bash)

rebuild_deb(deb, payload)
