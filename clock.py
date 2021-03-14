from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from time import strftime
from time import sleep
# import pyglet
# from playsound import playsound

# pyglet.font.add_file('DS-DIGIB.TTF')
# pyglet.font.add_file('digital-7 (mono).ttf')

root = Tk()
root.title('Digital Clock')
root.geometry('680x415+100+100')
root.config(bg='Black')
root.iconbitmap('pixmeadefavicon.ico')
label = Label(root, text="DIGITAL CLOCK",
              font=('Digital-7 Mono', '15',),
              background='Black',
              foreground='#50C9C3').place(x=80, y=42)


def alarm():
    newWindow = Toplevel()
    newWindow.title('Alarm')
    newWindow.geometry('430x385+800+100')
    newWindow.config(bg='Black')
    newWindow.iconbitmap('pixmeadefavicon.ico')

    def setalarm():

        while True:
            sleep(1)
            if int(inputh.get()) == int(strftime('%H')) and int(inputm.get()) == int(strftime('%M')):
                voltest()
                messagebox.showinfo('Alarm', 'Alarm Time')
                break
            else:
                pass

    lbl_alarm = Label(newWindow, text='ALARM', font=('DS-Digital', '45', 'bold'), background='#16222A',
                      foreground='#50C9C3', anchor='center')
    lbl_alarm.place(x=50, y=50, height=70, width=330)
    lbl_notice = Label(newWindow, text='Enter "HOUR" in 24hr format', font=('DS-Digital', '15',),
                       background='#16222A', foreground='#f64f59', anchor='center')
    lbl_notice.place(x=50, y=130, height=45, width=330)
    lbl_alhour = Label(newWindow, text='Hour ---->', font=('DS-Digital', '15',),
                       background='#16222A', foreground='#50C9C3', anchor='center')
    lbl_alhour.place(x=50, y=185, height=30, width=270)
    lbl_almin = Label(newWindow, text='Minute --->', font=('DS-Digital', '15',),
                      background='#16222A', foreground='#50C9C3', anchor='center')
    lbl_almin.place(x=50, y=225, height=30, width=270)

    c21 = Canvas(newWindow, bg="#16222A", height="10",
                 width='350', highlightthickness=0)
    c21.place(x=40, y=30)
    c22 = Canvas(newWindow, bg="#16222A", height="10",
                 width='350', highlightthickness=0)
    c22.place(x=40, y=345)
    c23 = Canvas(newWindow, bg="#16222A", height="325",
                 width='10', highlightthickness=0)
    c23.place(x=30, y=30)
    c24 = Canvas(newWindow, bg="#16222A", height="325",
                 width='10', highlightthickness=0)
    c24.place(x=390, y=30)

    inputh = Entry(newWindow, relief=SUNKEN, bd='0', font=('Digital-7 Mono', '15',),
                   bg='#16222A', fg='#50C9C3', highlightthickness='0')
    inputh.place(x=330, y=185, width=50, height=30)
    inputm = Entry(newWindow, relief=SUNKEN, bd='0', font=('Digital-7 Mono', '15',),
                   bg='#16222A', fg='#50C9C3', highlightthickness='0')
    inputm.place(x=330, y=225, width=50, height=30)

    bset_al = Button(newWindow, text='SET ALARM', relief=GROOVE, activebackground='#f64f59',
                     activeforeground='#16222A', bd='0', font=('Digital-7 Mono', '15',),
                     bg='#16222A', fg='#f64f59', highlightthickness='0', command=setalarm)
    bset_al.place(x=50, y=265, height=30, width=330)

    bcancel = Button(newWindow, text='CANCEL', relief=GROOVE, activebackground='#f64f59',
                     activeforeground='#16222A', bd='0', font=('Digital-7 Mono', '15',),
                     bg='#16222A', fg='#f64f59', highlightthickness='0', command=newWindow.destroy)
    bcancel.place(x=50, y=305, height=30, width=330)


def voltest():
    playsound('0451.wav', block=False)


def indicator_update():
    if int(strftime('%S')) % 2 == 1:
        indicator2.config(bg="Black")
        indicator1.config(bg="#50C9C3")

        c5.itemconfig(in23, fill="#f64f59")
        c5.itemconfig(in24, fill="#50C9C3")
        c5.itemconfig(in25, fill="#f64f59")
        c5.itemconfig(in26, fill="#50C9C3")
        c5.itemconfig(in28, fill="#f64f59")
        c5.itemconfig(in29, fill="#50C9C3")
        c5.itemconfig(in30, fill="#f64f59")
        c5.itemconfig(in31, fill="#50C9C3")
        c5.itemconfig(in32, fill="#f64f59")
        c5.itemconfig(in33, fill="#50C9C3")
        c5.itemconfig(in34, fill="#f64f59")
        c5.itemconfig(in35, fill="#50C9C3")
        c5.itemconfig(in36, fill="#f64f59")
        c5.itemconfig(in37, fill="#50C9C3")
        c5.itemconfig(in38, fill="#f64f59")
        c5.itemconfig(in39, fill="#50C9C3")
        c5.itemconfig(in40, fill="#f64f59")
        c6.itemconfig(in41, fill="#f64f59")  # endofup
        c6.itemconfig(in42, fill="#50C9C3")
        c6.itemconfig(in43, fill="#f64f59")
        c6.itemconfig(in44, fill="#50C9C3")
        c6.itemconfig(in45, fill="#f64f59")
        c6.itemconfig(in46, fill="#50C9C3")
        c6.itemconfig(in47, fill="#f64f59")
        c6.itemconfig(in48, fill="#50C9C3")
        c6.itemconfig(in49, fill="#f64f59")
        c6.itemconfig(in50, fill="#50C9C3")
        c6.itemconfig(in51, fill="#f64f59")
        c6.itemconfig(in52, fill="#50C9C3")
        c6.itemconfig(in53, fill="#f64f59")
        c6.itemconfig(in54, fill="#50C9C3")
        c6.itemconfig(in55, fill="#f64f59")
        c6.itemconfig(in56, fill="#50C9C3")
        c6.itemconfig(in57, fill="#f64f59")

    else:
        indicator1.config(bg="Black")
        indicator2.config(bg="#f64f59")

        c6.itemconfig(in41, fill="#50C9C3")
        c6.itemconfig(in42, fill="#f64f59")
        c6.itemconfig(in43, fill="#50C9C3")
        c6.itemconfig(in44, fill="#f64f59")
        c6.itemconfig(in45, fill="#50C9C3")
        c6.itemconfig(in46, fill="#f64f59")
        c6.itemconfig(in47, fill="#50C9C3")
        c6.itemconfig(in48, fill="#f64f59")
        c6.itemconfig(in49, fill="#50C9C3")
        c6.itemconfig(in50, fill="#f64f59")
        c6.itemconfig(in51, fill="#50C9C3")
        c6.itemconfig(in52, fill="#f64f59")
        c6.itemconfig(in53, fill="#50C9C3")
        c6.itemconfig(in54, fill="#f64f59")
        c6.itemconfig(in55, fill="#50C9C3")
        c6.itemconfig(in56, fill="#f64f59")
        c6.itemconfig(in57, fill="#50C9C3")
        c5.itemconfig(in23, fill="#50C9C3")  # startofup
        c5.itemconfig(in24, fill="#f64f59")
        c5.itemconfig(in25, fill="#50C9C3")
        c5.itemconfig(in26, fill="#f64f59")
        c5.itemconfig(in28, fill="#50C9C3")
        c5.itemconfig(in29, fill="#f64f59")
        c5.itemconfig(in30, fill="#50C9C3")
        c5.itemconfig(in31, fill="#f64f59")
        c5.itemconfig(in32, fill="#50C9C3")
        c5.itemconfig(in33, fill="#f64f59")
        c5.itemconfig(in34, fill="#50C9C3")
        c5.itemconfig(in35, fill="#f64f59")
        c5.itemconfig(in36, fill="#50C9C3")
        c5.itemconfig(in37, fill="#f64f59")
        c5.itemconfig(in38, fill="#50C9C3")
        c5.itemconfig(in39, fill="#f64f59")
        c5.itemconfig(in40, fill="#50C9C3")


def time_show():
    hour = strftime('%I:')
    mins = strftime('%M')
    sec = strftime('%S')
    day = strftime('%A')
    fulldate = strftime('%d-%b-%G')

    if int(strftime('%H')) >= 12:
        ampmholder = 'PM'
    else:
        ampmholder = 'AM'

    lbl_hour.config(text=hour)
    lbl_min.config(text=mins)
    lbl_sec.config(text=sec)
    lbl_ampm.config(text=ampmholder)
    lbl_fulldate.config(text=fulldate)
    lbl_day.config(text=day)

    indicator_update()

    lbl_hour.after(1000, time_show)


# Labels
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

lbl_fulldate = Label(root, font=('DS-Digital', '20', 'bold'), background='#16222A',
                     foreground='#50C9C3', anchor='center')
lbl_fulldate.place(x=290, y=285, height=30, width=200)

lbl_day = Label(root, font=('DS-Digital', '20', 'bold'), background='#16222A',
                foreground='#50C9C3', anchor='center')
lbl_day.place(x=80, y=285, height=30, width=200)

lbl_12hrc = Label(root, text="12 HOUR", font=('Digital-7 Mono', '15',),
                  background='Black', foreground='#50C9C3').place(x=534, y=40)

# boundries
c1 = Canvas(root, bg="#16222A", height="10", width='540', highlightthickness=0)
c1.place(x=70, y=365)
c2 = Canvas(root, bg="#16222A", height="10", width='540', highlightthickness=0)
c2.place(x=70, y=30)
c3 = Canvas(root, bg="#16222A", height="345", width='10', highlightthickness=0)
c3.place(x=60, y=30)
c4 = Canvas(root, bg="#16222A", height="345", width='10', highlightthickness=0)
c4.place(x=610, y=30)

# buttons
balarm = Button(root, text='ALARM', relief=GROOVE, activebackground='#f64f59',
                activeforeground='#16222A', bd='0', font=('Digital-7 Mono', '15',),
                bg='#16222A', fg='#f64f59', highlightthickness='0', command=alarm)
balarm.place(x=80, y=325, height=30, width=200)

bvoltest = Button(root, text='Volume Test', relief=GROOVE, activebackground='#f64f59',
                  activeforeground='#16222A', bd='0', command=voltest,
                  font=('Digital-7 Mono', '15',), bg='#16222A', fg='#f64f59', highlightthickness='0')
bvoltest.place(x=290, y=325, height=30, width=200)

bclose = Button(root, text='CLOSE', relief=GROOVE, activebackground='#f64f59',
                activeforeground='#16222A', bd='0', command=root.destroy,
                font=('Digital-7 Mono', '15',), bg='#16222A', fg='#f64f59', highlightthickness='0')
bclose.place(x=500, y=325, height=30, width=100)

# indicators
indicator1 = Canvas(root, bg="#50C9C3", height="7",
                    width='95', highlightthickness=0)
indicator2 = Canvas(root, bg="#50C9C3", height="7",
                    width='95', highlightthickness=0)
indicator1.place(x=290, y=50)
indicator2.place(x=395, y=50)

c5 = Canvas(root, bg="Black", height="15", width='100', highlightthickness=0)
in23 = c5.create_rectangle(3, 0, 5, 30, fill='Black', width='0')
in24 = c5.create_rectangle(9, 0, 11, 30, fill='Black', width='0')
in25 = c5.create_rectangle(15, 0, 17, 30, fill='Black', width='0')
in26 = c5.create_rectangle(21, 0, 23, 30, fill='Black', width='0')
in28 = c5.create_rectangle(27, 0, 29, 30, fill='Black', width='0')
in29 = c5.create_rectangle(33, 0, 35, 30, fill='Black', width='0')
in30 = c5.create_rectangle(39, 0, 41, 30, fill='Black', width='0')
in31 = c5.create_rectangle(45, 0, 47, 30, fill='Black', width='0')
in32 = c5.create_rectangle(51, 0, 53, 30, fill='Black', width='0')
in33 = c5.create_rectangle(57, 0, 59, 30, fill='Black', width='0')
in34 = c5.create_rectangle(63, 0, 65, 30, fill='Black', width='0')
in35 = c5.create_rectangle(69, 0, 71, 30, fill='Black', width='0')
in36 = c5.create_rectangle(75, 0, 77, 30, fill='Black', width='0')
in37 = c5.create_rectangle(81, 0, 83, 30, fill='Black', width='0')
in38 = c5.create_rectangle(87, 0, 89, 30, fill='Black', width='0')
in39 = c5.create_rectangle(93, 0, 95, 30, fill='Black', width='0')
in40 = c5.create_rectangle(99, 0, 101, 30, fill='Black', width='0')
c5.place(x=500, y=285)

c6 = Canvas(root, bg='Black', height="15", width='100', highlightthickness=0)
in41 = c6.create_rectangle(0, 0, 2, 30, fill='Black', width='0')
in42 = c6.create_rectangle(6, 0, 8, 30, fill='Black', width='0')
in43 = c6.create_rectangle(12, 0, 14, 30, fill='Black', width='0')
in44 = c6.create_rectangle(18, 0, 20, 30, fill='Black', width='0')
in45 = c6.create_rectangle(24, 0, 26, 30, fill='Black', width='0')
in46 = c6.create_rectangle(30, 0, 32, 33, fill='Black', width='0')
in47 = c6.create_rectangle(36, 0, 38, 30, fill='Black', width='0')
in48 = c6.create_rectangle(42, 0, 44, 30, fill='Black', width='0')
in49 = c6.create_rectangle(48, 0, 50, 30, fill='Black', width='0')
in50 = c6.create_rectangle(54, 0, 56, 30, fill='Black', width='0')
in51 = c6.create_rectangle(60, 0, 62, 33, fill='Black', width='0')
in52 = c6.create_rectangle(66, 0, 68, 30, fill='Black', width='0')
in53 = c6.create_rectangle(72, 0, 74, 30, fill='Black', width='0')
in54 = c6.create_rectangle(78, 0, 80, 30, fill='Black', width='0')
in55 = c6.create_rectangle(84, 0, 86, 30, fill='Black', width='0')
in56 = c6.create_rectangle(90, 0, 92, 33, fill='Black', width='0')
in57 = c6.create_rectangle(96, 0, 98, 30, fill='Black', width='0')
c6.place(x=500, y=300)

time_show()

root.mainloop()
