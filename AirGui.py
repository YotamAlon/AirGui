#Kivy imports
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty

#other imports
from subproces import check_output

def AireplayScreen(Screen):
    pass

def AirodumpScreen(Screen):
    pass

def AirmonScreen(Screen):
	interfaces = ListProperty()
	processes = ListProperty()
		
    def __init__(self, **kwargs):
		super(AirmonScreen, self).__init__(kwargs)
		get_interfaces()
		get_processes()
	
	def get_interfaces():
		interfaces = check_output("airmon-ng", shell=True).split('\n')
		for i in range(1, len(interfaces)):
			self.interfaces.append(interfaces[i].split('\t')[1])
			
	def get_processes():
		processes = check_output("airmon-ng check " + interface, shell=True).split('\n')
		for i in range(6, len(processes)):
			self.processes.append(processes[i].split(' '))

def GuiManager(ScreenManager):
    pass

def AirGui(App):
    def build():
        return GuiManager()

if __name__ == "__main__":
    AirGui().run()
