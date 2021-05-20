from tkinter import *
import os
import time


root = Tk()


# Screen size
root.geometry("956x616")
root.maxsize(956,616)
root.minsize(956,616)

# Setting the title
root.title("TechOS")

def open_start():
    exit()

def open_Code_Editor():
    os.system("python notepad.py")


def open_Calculator():
    os.system("python calc.py")

def open_File_Explorer():
    os.system("python fileBrowser.py")

def open_Terminal():
    os.system("python terminal.py")

def App_Installer():
	os.system("python app_installer.py")
def Music_Player():
	os.system("python musicPlayer.py")
# Creating the start menu


start_menu = Menu(root)
dropdown = Menu(start_menu, tearoff=0)
dropdown.add_command(label="Shutdown", command=open_start)
dropdown.add_command(label="Code Editor", command=open_Code_Editor)
dropdown.add_command(label="Calculator", command=open_Calculator)
dropdown.add_command(label="File Explorer", command=open_File_Explorer)
dropdown.add_command(label="Terminal", command=open_Terminal)
dropdown.add_command(label="App Installer", command=App_Installer)
dropdown.add_command(label="Music Player", command=Music_Player)

root.config(menu=start_menu)


start_menu.add_cascade(label="Start", menu=dropdown)


root.mainloop()