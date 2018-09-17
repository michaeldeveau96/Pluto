from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class InitializerScreen(Screen):
    
    def startup(self):
        username = TextInput(text='Enter router username: ')
        password = TextInput(text='Enter router password: ')
    pass
