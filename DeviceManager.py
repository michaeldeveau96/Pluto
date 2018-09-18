from kivy.uix.screenmanager import Screen
import nmap
import os
import subprocess
from scapy.all import *
import sys

from scapy.layers.l2 import Ether, ARP

class DeviceManager(Screen):

    def get_neighbors(self):
        output = subprocess.Popen(["nmap", "-sP", "192.168.0.*"], stdout=subprocess.PIPE)
        netView = output.stdout.read().decode('utf-8')
        for line in netView.split('\n'):
            if 'MAC Address' in line:
                mac = line.split(': ', 1)[1]
                mac = mac.split('\r', 1)[0]
                macs = [mac]
                print(macs)

        for line in netView.split('\n'):
            if 'Nmap scan report' in line:
                ip = line.split('r ', 1)[1]
                ip = ip.split('\r', 1)[0]
                ips = [ip]
                print(ips)

