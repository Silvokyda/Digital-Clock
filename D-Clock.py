from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Digital Clock')

label = Label(root, font = ('aerial', 30), background ='blue', foreground ='red')

def time():
	string = strftime('%H:%M:%S')
	label.config(text=string)
	label.after(1, time)

label.pack(anchor ='center')

time()
