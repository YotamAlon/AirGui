from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


def AireplayScreen(Screen):
    pass

def AirodumpScreen(Screen):
    pass

def AirmonScreen(Screen):
    pass

def GuiManager(ScreenManager):
    pass

def AirGui(App):
    def build():
        return GuiManager()

if __name__ == "__main__":
    AirGui().run()