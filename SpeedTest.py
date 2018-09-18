import os
import pyspeedtest

from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class SpeedTest(Screen):
    speed = ObjectProperty()


    def test(self):
        layout = BoxLayout(padding=10)
        st = pyspeedtest.SpeedTest()
        ping = st.ping()
        print("Ping: " + str(int(ping)) + " ms")
        self.speed.add_widget(Label(text="Ping: " + str(int(ping)) + " ms"))

        down = round(st.download(),2)
        downMbps = down * 0.000001
        print("Download: " + str(int(downMbps)) + ' Mbps')
        self.speed.add_widget(Label(text="Download: " + str(int(downMbps)) + ' Mbps'))

        up = round(st.upload(),2)
        upMbps = up * 0.000001
        print("Upload: " + str(int(upMbps)) + ' Mbps')
        self.speed.add_widget(Label(text="Upload: " + str(int(upMbps)) + ' Mbps'))


    def processSpeeds(self):
        pass