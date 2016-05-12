import os

import configparser

configfile = os.path.abspath(os.path.join(os.path.dirname(__file__), '../virt-create.conf'))
config = configparser.ConfigParser()


def readconfig(filename):
    config.read([filename, configfile])


def writeconfig(conf=config):
    configdir = os.path.dirname(configfile)
    if not os.path.isdir(configdir):
        os.makedirs(configdir, exist_ok=True)
    with open(configfile, 'w') as f:
        conf.write(f)
