#!/usr/bin/python

import argparse

import virtcreate.config as config


class VirtCreate:
    def createArgumentParser(self):
        """
        Create argument-parser

        :return: parser instance
        """
        parser = argparse.ArgumentParser(description='Create virtual Machines')
        parser.add_argument('-v', help='do verbose output', action='store_true')
        parser.add_argument('-c', dest='config', type=str, default='/etc/virt-create.conf',
                            help='path to virt-create configfile')
        parser.add_argument('-n', dest='hostname', type=str, help='name of vm', required=True)
        parser.add_argument('-d', dest='domainname', type=str, help='domainname of newly created host')
        parser.add_argument('-s', dest='vm_size', type=str, help='size of created vm in GB')
        parser.add_argument('--ram', dest='ram', type=str, help='amount of ram for the new vm')
        parser.add_argument('--vcpu', dest='vcpu', type=str, help='count of virtual cpus')
        return parser

    def create_command(self, args):
        '''
        Create command to create virtual machine

        :param args: the programm arguments
        :return: the command to run
        '''
        # virt_install.bake('--{}'.format(argname), '')
        # for key, value in config.config['virt_machine'].iteritems():
        #    print(key, value)


        # print(virt_install)


        # cmd = '''/usr/bin/virt-install \
        #        --connect=qemu:///system \
        #        --name={0} \
        #        --ram={3} \
        #        --vcpus={2} \
        #        --os-type=linux \
        #        --os-variant=debianwheezy \
        #        --disk /dev/vg_data/lv_{0},bus=virtio,size={1} \
        #        --network='network=10-server,model=virtio' \
        #        --hvm \
        #        --vnc \
        #        --noautoconsole \
        #        --keymap=de \
        #        --location http://ftp.de.debian.org/debian/dists/stable/main/installer-amd64 \
        #        --extra-args="auto=true hostname={0} domain=einsle.de url=http://www.einsle.de/wheezy-test.cfg"'''
        # cmd = cmd.format(args.name.lower(), args.size, args.cpu, args.ram)
        # return cmd

    def parse_arguments(self, args):
        config.readconfig(args.config)
        cfg = dict()
        cfg['domainname'] = args.domainname if args.domainname else config.config['config']['domainname']
        cfg['vm_size'] = args.vm_size if args.vm_size else config.config['config']['vm_size']
        cfg['ram'] = args.ram if args.ram else config.config['config']['ram']
        cfg['vcpu'] = args.vcpu if args.vcpu else config.config['config']['vcpu']
        return cfg

    def main(self):
        parser = self.createArgumentParser()
        args = parser.parse_args()
        # cmd = self.createCommand(args)
        cfg = self.parse_arguments(args)
        if args.v:
            print("Configpath:   {0}".format(args.config))
            print("Hostname:     {0}".format(args.hostname.lower()))
            print("Domainname:   {0}".format(cfg['domainname']))
            print("VM Size:      {0} GB".format(cfg['vm_size']))
            print("Ram:          {0}".format(cfg['ram']))
            print("vCPU Count:   {0}".format(cfg['vcpu']))


def entry_point():
    VirtCreate().main()


if __name__ == "__main__":
    entry_point()
