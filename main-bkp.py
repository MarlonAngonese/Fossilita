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

class OtherScreen(MDScreen):
    pass

class Test(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.screen = Builder.load_file('./main.kv')

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.set_item(x),
            } for i in range(5)
        ]

        self.menu = MDDropdownMenu(
            caller = self.screen.get_screen('volumetria').ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu.bind()

    def set_item(self, text_item):
        self.screen.get_screen('volumetria').ids.drop_item.set_item(text_item)
        self.menu.dismiss()

    def build(self):
        return self.screen


Test().run()