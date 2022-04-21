from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen

class Manager(ScreenManager): 
    pass

class VolumetriaScreen(MDScreen):
    pass

class Test(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.screen = Builder.load_file('./main.kv')

    def build(self):
        return self.screen

Test().run()