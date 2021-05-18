from tkinter import *
from tkinter.ttk import *
from time import strftime

Clock = Tk()
Clock.title("Clock By M074MED")


clock_label = Label(Clock, font=("", 80), background="black", foreground="cyan")
clock_label.pack(anchor="center")


def time():
    string = strftime("%I:%M:%S %p\n%root %d/%m/%Y")
    clock_label.config(text=string)
    clock_label.after(1000, time)


time()

mainloop()
