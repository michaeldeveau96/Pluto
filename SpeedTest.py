import os
import pyspeedtest

from kivy.uix.screenmanager import Screen


class SpeedTest(Screen):

    def test(self):
        st = pyspeedtest.SpeedTest()
        ping = st.ping()
        print("Ping: " + str(int(ping)) + " ms")
        down = round(st.download(),2)
        downMbps = down * 0.000001
        print("Download: " + str(int(downMbps)) + ' Mbps')
        up = round(st.upload(),2)
        upMbps = up * 0.000001
        print("Upload: " + str(int(upMbps)) + ' Mbps')