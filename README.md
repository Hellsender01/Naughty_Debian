# Naughty Debian
Simple script to inject bash script inside any debian package. It utilises preinst and postinst scripts as a medium to run user defined bash script. **This script depends on dpkg-deb** command line to achieve it's task, so make sure you have it on your system.

# Install
```bash
git clone https://github.com/Hellsender01/Naughty_Debian.git
cd Naughty_Debian/
python3 -m pip install -r requirements.txt
sudo chmod +x naughty_debian.py
./naughty_debian.py
```
# Help
```
$./naughty_debian.py --help
usage: ./naughty_debian.py -d debian_package -b bash_file

Inject bash scripts in debian packages.

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      show program's version number and exit
  -d debian package  target debian package
  -b bash script     bash script containing payload

EXAMPLE - ./naughty_debian.py -d /tmp/file.deb -b /tmp/script.sh
```
