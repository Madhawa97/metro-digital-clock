from time import strftime
from tkinter import *
from tkinter.ttk import *
# from multiprocessing import Process
# import pyglet  # pip install pyglet
# from playsound import playsound

# pyglet.font.add_file('digital-7 (mono).ttf')

# creating tkinter window
root = Tk()
root.title('Digital Clock')
# root.title("ඔරලෝසුව")
root.geometry('600x600')
root.config(bg='#753a88')

label = Label(root, text="DIGITAL CLOCK",
              font=('Digital-7 Mono', '10',),
              background='Black',
              foreground='#2193b0').pack(anchor='center')


def time():
    string = strftime('%H:%M:%S %n%A %n%d-%b-%G')
    lbl.config(text=string)
    lbl.after(1000, time)


def play_alarm():
    # while True:
    if alarm.get() == 1:
        playsound('0451.wav', block=False)
    else:
        pass


lbl = Label(root, font=('Digital-7 Mono', '35', 'bold'),
            background='Black',
            foreground='#2193b0')

lbl.pack(anchor='center')

alarm = IntVar()
alarm.set(1)

rb1 = Radiobutton(root, text='On',
                  variable=alarm,
                  value=1,
                  command=print(alarm.get())
                  )
rb2 = Radiobutton(root, text='Off',
                  variable=alarm,
                  value=2,
                  command=print(alarm.get())
                  )
rb1.pack()
rb2.pack()
c = Canvas(root, bg="Red", height="700", width='700').pack()

time()

root.mainloop()
