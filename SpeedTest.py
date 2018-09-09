import os

from kivy.uix.screenmanager import Screen


class SpeedTest(Screen):

    def test(self):
        os.system('ipconfig')

    pass