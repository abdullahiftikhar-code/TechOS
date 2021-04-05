from tkinter import *
import os
import time
from tkinter.messagebox import showinfo


def install():
	global app_to_install
	try:
		os.system(f"choco install {app_to_install}")
	except Exception as e:
		showinfo("Not Found", "Package not found")
	

root = Tk()
root.geometry("956x616")
root.maxsize(956,616)
root.minsize(956,616)
root.title("App installer (using choco make sure to use correct package name)")

app_to_install = Entry(root)
app_to_install.pack()
app_to_install.focus_set()


install = Button(root,text='install', command=install)
install.pack(side='bottom')



root.mainloop()