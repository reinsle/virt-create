import configparser
import os

configfile = os.path.expanduser('/etc/virt-create/virt-create.conf')
config = configparser.ConfigParser()
config['virt_machine'] = {
    'lv_prefix': 'vm_',
    'vm_network': 'network=10-server,model=virtio',
    'autoinst_url': 'http://www.einsle.de/wheezy-test.cfg',
    'vm_domain': 'einsle.de',
    'vm_keymap': 'de',
    'vm_default_cpu_count': '1',
    'vm_default_cpu_ram': '256',
    'installer_location': 'http://ftp.de.debian.org/debian/dists/stable/main/installer-amd64'}
config['testerle'] = {}


def readconfig():
    config.read([configfile, ])


def writeconfig(conf=config):
    configdir = os.path.dirname(configfile)
    if not os.path.isdir(configdir):
        os.makedirs(configdir, exist_ok=True)
    with open(configfile, 'w') as f:
        conf.write(f)


readconfig()
