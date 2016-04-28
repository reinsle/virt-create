import configparser
import os

configfile = os.path.expanduser('/etc/virt-create/virt-create.conf')
config = configparser.ConfigParser()
config['section1'] = {'default1': 'invalid',
                    'default2': 'invalid',
                    'default3': 'invalid',
                    'default4': 'invalid',
                    'default5': 'invalid'}
config['section2'] = {}


def readconfig():
    config.read([configfile, ])


def writeconfig(conf=config):
    configdir = os.path.dirname(configfile)
    if not os.path.isdir(configdir):
        os.makedirs(configdir, exist_ok=True)
    with open(configfile, 'w') as f:
        conf.write(f)


readconfig()