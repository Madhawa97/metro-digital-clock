from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("ඔරලෝසුව")


def time():
    string = strftime('%H:%M:%S %n%b %d %G - %A ')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('arial', '35', 'bold italic'),
            background='blue',
            foreground='yellow')

lbl.pack(anchor='center')

time()

root.mainloop()
