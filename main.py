import os

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from HomeScreen import HomeScreen
from SpeedTest import SpeedTest
from BandwidthMonitor import BandwidthMonitor
from ParentalControls import ParentalControls
from DeviceManager import DeviceManager
from InitializerScreen import InitializerScreen
from ScreenManagement import ScreenManager


pluto = Builder.load_file('pluto.kv')


class MyApp(App):

    def build(self):
        return pluto


if __name__ == '__main__':
    MyApp().run()
