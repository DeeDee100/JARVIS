import os
import subprocess as sp

paths = {
	'notepad': "C:\\Windows\\system32\\notepad.exe",
	'discord': "C:\\Users\\amand\\AppData\\Local\Discord\\app-1.0.9003\\Discord.exe"
	
}

def open_notepad():
	os.startfile(paths['notepad'])
	
def open_discord():
	os.startfile(paths['discord'])

def open_terminal():
	os.system('start wt')

def open_edge():
	os.system('start MicrosoftEdge')

