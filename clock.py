import sys
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import time
from time import strftime
#import pyglet, os  # pip install pyglet
##from playsound import playsound

import datetime

#pyglet.font.add_file('DS-DIGIB.TTF')

root = Tk()
root.title('Digital Clock')
root.geometry('680x500')
root.config(bg='Black')
label = Label(root, text="DIGITAL CLOCK",
              font=('Digital-7 Mono', '15',),
              background='Black',
              foreground='#50C9C3').place(x=80, y=40)


def alarm():
    global inputh, inputm
    newWindow = Toplevel()
    newWindow.title('Alarm')
    newWindow.geometry('500x400')
    newWindow.config(bg='Black')
    lbl_alarm = Label(newWindow, text='ALARM', font=('DS-Digital', '45', 'bold'), background='#16222A',
                      foreground='#50C9C3', anchor='center')
    lbl_alarm.place(x=180, y=10, height=90, width=100)

    inputh = Entry(newWindow, relief=SUNKEN, bd='0', font=('Digital-7 Mono', '15',),
                   bg='#16222A', fg='#50C9C3', highlightthickness='0')
    inputh.place(x=80, y=30, width=30, height=20)
    inputm = Entry(newWindow, relief=SUNKEN, bd='0', font=('Digital-7 Mono', '15',),
                   bg='#16222A', fg='#50C9C3', highlightthickness='0')
    inputm.place(x=80, y=65, width=30, height=20)
    set_al = Button(newWindow, text='SET ALARM', relief=GROOVE, activebackground='#50C9C3',
                    activeforeground='#16222A', height=1, width=11, bd='0', font=('Digital-7 Mono', '15',),
                    bg='#16222A', fg='#50C9C3', highlightthickness='0', command=setalarm)
    set_al.place(x=80, y=100)


def setalarm():
    global inputh, inputm
    h = inputh.get()
    m = inputm.get()
    while (1):
        if int(h) == datetime.datetime.now().hour and int(m) == datetime.datetime.now().minute:
            playsound('0451.wav')
            break


def voltest():
    playsound('0451.wav', block=False)


def time_show():
    # string = strftime('%H:%M:%S %n%A %n%d-%b-%G')
    hour = strftime('%I:')
    min = strftime('%M')
    sec = strftime('%S')

    lbl_hour.config(text=hour)
    lbl_min.config(text=min)
    lbl_sec.config(text=sec)
    lbl_ampm.config(text=ampmholder)
    if int(strftime('%S')) % 2 == 1:
        indicator2.config(bg="Black")
        indicator1.config(bg="#50C9C3")
        indicator1.place(x=290, y=50)
    else:
        indicator1.config(bg="Black")
        indicator2.config(bg="#50C9C3")
        indicator2.place(x=395, y=50)

    lbl_hour.after(1000, time_show)


lbl_hour = Label(root, font=('DS-Digital', '120', 'bold'), background='#16222A',
                 foreground='#50C9C3', anchor='e')
lbl_hour.place(x=80, y=75, height=200, width=200)

lbl_min = Label(root, font=('DS-Digital', '120', 'bold'), background='#16222A',
                foreground='#50C9C3', anchor='e', padx=18)
lbl_min.place(x=290, y=75, height=200, width=200)

lbl_sec = Label(root, font=('DS-Digital', '45', 'bold'), background='#16222A',
                foreground='#50C9C3', anchor='e', padx=17)
lbl_sec.place(x=500, y=175, height=100, width=100)

lbl_ampm = Label(root, font=('DS-Digital', '45', 'bold'), background='#16222A',
                 foreground='#50C9C3', anchor='center')
lbl_ampm.place(x=500, y=75, height=90, width=100)

if int(strftime('%H')) >= 12:
    ampmholder = 'PM'
else:
    ampmholder = 'AM'

# unfunctional label
lbl_12hrc = Label(root, text="12 HOUR", font=('Digital-7 Mono', '15',),
                  background='Black', foreground='#50C9C3').place(x=533, y=40)

# boundries
c1 = Canvas(root, bg="#16222A", height="10", width='540', highlightthickness=0)
c1.place(x=70, y=285)
c2 = Canvas(root, bg="#16222A", height="10", width='540', highlightthickness=0)
c2.place(x=70, y=30)
c3 = Canvas(root, bg="#16222A", height="265", width='10', highlightthickness=0)
c3.place(x=60, y=30)
c4 = Canvas(root, bg="#16222A", height="265", width='10', highlightthickness=0)
c4.place(x=610, y=30)

balarm = Button(root, text='ALARM', relief=GROOVE, activebackground='#50C9C3',
                activeforeground='#16222A', height=1, width=22, bd='0', font=('Digital-7 Mono', '15',),
                bg='#16222A', fg='#50C9C3', highlightthickness='0', command=alarm)
balarm.place(x=80, y=305)

bvoltest = Button(root, text='Vol Test', relief=GROOVE, activebackground='#50C9C3',
                  activeforeground='#16222A', height=1, width=11, bd='0', command=voltest,
                  font=('Digital-7 Mono', '15',), bg='#16222A', fg='#50C9C3', highlightthickness='0')
bvoltest.place(x=290, y=305)
'''
b24hr = Button(root, text='24 HR', relief=GROOVE, activebackground='#50C9C3',
               activeforeground='#16222A', height=1, width=11, bd='0',
               font=('Digital-7 Mono', '15',), bg='#16222A', fg='#50C9C3', highlightthickness='0')
b24hr.place(x=400, y=305)
'''
indicator1 = Canvas(root, bg="#50C9C3", height="6",
                    width='95', highlightthickness=0)
indicator2 = Canvas(root, bg="#50C9C3", height="6",
                    width='95', highlightthickness=0)

time_show()

root.mainloop()
