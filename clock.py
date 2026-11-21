from tkinter import *
from tkinter.ttk import *

from time import strftime

wndw=Tk()
wndw.title("clock")

def time():
    h=int(strftime('%H'))
    m=strftime('%M')
    s=strftime('%S')

    ampm="AM" if h < 12 else "PM"
    h=h % 12
    string= f"{h}:{m}:{s}{ampm}"

    lbl.config(text=string)

    lbl.after(1000,time)

lbl=Label(wndw,font=("calibri",40,"bold"),background="green", foreground="red")
lbl.pack() 
time()

wndw.mainloop()