#!/usr/bin/python

import argparse
import os

class VirtCreate:
    def createArgumentParser(self):
        """
        Create argument-parser

        :return: parser instance
        """
        parser = argparse.ArgumentParser(description='Create virtual Machines')
        parser.add_argument('-n', dest='name', type=str, help='name of vm', required=True)
        parser.add_argument('-s', dest='size', type=int, default=15,
                   help='size of created vm in GB')
        parser.add_argument('-c', dest='cpu', type=int, default=1,
                   help='numbers of cpus for vm')
        parser.add_argument('-r', dest='ram', type=int, default=512,
                   help='size of ram')
        parser.add_argument('-v', help='do verbose output', action='store_true')
        return parser

    def createCommand(self, args):
        '''
        Create command to create virtual machine

        :param args: the programm arguments
        :return: the command to run
        '''
        cmd = '''/usr/bin/virt-install \
                --connect=qemu:///system \
                -n {0} \
                -r {3} \
                --vcpus={2} \
                --os-type=linux \
                --os-variant=debianwheezy \
                --disk /dev/vg_data/lv_{0},bus=virtio,size={1} \
                -w network=10-server,model=virtio \
                --hvm \
                --vnc \
                --noautoconsole \
                --keymap=de \
                --location http://ftp.de.debian.org/debian/dists/stable/main/installer-amd64 \
                --extra-args="auto=true hostname={0} domain=einsle.de url=http://www.einsle.de/wheezy-test.cfg"'''
        cmd = cmd.format(args.name.lower(), args.size, args.cpu, args.ram)
        return cmd

    def main(self):
        parser = self.createArgumentParser()
        args = parser.parse_args()
        cmd = self.createCommand(args)
        if args.v:
            print("Name: {0}".format(args.name.lower()))
            print("Size: {0}".format(args.size))
            print("Cpu:  {0}".format(args.cpu))
            print("Ram:  {0}".format(args.ram))
            print("Cmd:  {0}".format(cmd))
        os.system(cmd)

if __name__ == "__main__":
    VirtCreate().main()
