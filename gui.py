"""Code graphic interface with TKinter"""

from tkinter import Tk, Label, Button, Entry, Canvas
from tkinter import filedialog
import uteis

WINDOW = Tk()

WINDOW.title("Ip Map SSH")

HEADER = Label(WINDOW, text="Ip Map SSH", background="blue")
HEADER.place(x=200, y=40)

#____________________________Buttons________________________#

def upload_action():
    """Upload files"""
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def bt_click():
    """get info function"""
    uteis.lookip(IP_ENTER.get(), LOGIN_ENTER.get(), PASSWORD_ENTER.get(), SHELL_ENTER.get())

#______________________________ip___________________________#
IP_LABEL = Label(WINDOW, text="IP:")
IP_LABEL.place(x=50, y=100)
IP_ENTER = Entry(WINDOW)
IP_ENTER.place(x=90, y=100)

#_____________________________port___________________________#
PORT_LABEL = Label(WINDOW, text="Port:")
PORT_LABEL.place(x=240, y=100)

PORT_ENTER = Entry(WINDOW)
PORT_ENTER.place(x=300, y=100)

#_____________________________login___________________________#
LOGIN_LABEL = Label(WINDOW, text="Login:")
LOGIN_LABEL.place(x=50, y=140)

LOGIN_ENTER = Entry(WINDOW)
LOGIN_ENTER.place(x=90, y=140)

#_____________________________password________________________#
PASSWORD_LABEL = Label(WINDOW, text="Password:")
PASSWORD_LABEL.place(x=240, y=140)

PASSWORD_ENTER = Entry(WINDOW)
PASSWORD_ENTER.place(x=300, y=140)

#__________________________command_shell_______________________#
LINE1 = Canvas(WINDOW, width=400, height=1, background="grey")
LINE1.place(x=35, y=180)

SHELL_LABEL = Label(WINDOW, text="Command Shell:")
SHELL_LABEL.place(x=50, y=210)

SHELL_ENTER = Entry(WINDOW)
SHELL_ENTER.place(x=140, y=210, width=287)

#__________________________enterFile_______________________#
LINE2 = Canvas(WINDOW, width=400, height=1, background="grey")
LINE2.place(x=35, y=250)

LB6 = Label(WINDOW, text="File Brutal force:")
LB6.place(x=50, y=280)

BUTTON = Button(WINDOW, text='File.txt', command=upload_action).place(x=180, y=275)

LINE3 = Canvas(WINDOW, width=400, height=1, background="grey")
LINE3.place(x=35, y=310)

BUTTON2 = Button(WINDOW, text='Submit!', command=bt_click).place(x=210, y=370)

###############################
#Size window and position
WINDOW.geometry("480x450+300+300")
WINDOW.mainloop()
