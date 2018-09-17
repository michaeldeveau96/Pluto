from kivy.uix.screenmanager import Screen
import nmap

class DeviceManager(Screen):

    def get_neighbors(self):
        nm = nmap.PortScanner()
        print(nm.all_hosts())
    pass
