from tkinter import *
from functools import partial
from tkinter import filedialog
import uteis

janela = Tk()

janela.title("Ip Map SSH")

header = Label(janela, text="Ip Map SSH", background="blue")
header.place(x=200, y=40)

#____________________________Buttons________________________#

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def bt_click():
    uteis.lookip(ip_enter.get(), port_enter.get(), login_enter.get(), password_enter.get(), shell_enter.get())


#______________________________ip___________________________#
ip_label = Label(janela, text="IP:")
ip_label.place(x=50, y=100)

ip_enter = Entry(janela)
ip_enter.place(x=90, y=100)

#_____________________________port___________________________#
port_label = Label(janela, text="Port:")
port_label.place(x=240, y=100)

port_enter = Entry(janela)
port_enter.place(x=300, y=100)

#_____________________________login___________________________#
login_label = Label(janela, text="Login:")
login_label.place(x=50, y=140)

login_enter = Entry(janela)
login_enter.place(x=90, y=140)

#_____________________________password________________________#
password_label = Label(janela, text="Password:")
password_label.place(x=240, y=140)

password_enter = Entry(janela)
password_enter.place(x=300, y=140)

#__________________________command_shell_______________________#
line1 = Canvas(janela, width=400, height=1, background="grey")
line1.place(x=35, y=180)

shell_label = Label(janela, text="Command Shell:")
shell_label.place(x=50, y=210)

shell_enter = Entry(janela)
shell_enter.place(x=140, y=210, width=287)

#__________________________enterFile_______________________#
line2 = Canvas(janela, width=400, height=1, background="grey")
line2.place(x=35, y=250)

lb6 = Label(janela, text="File Brutal force:")
lb6.place(x=50, y=280)

button = Button(janela, text='File.txt', command=UploadAction).place(x=180, y=275)

line3 = Canvas(janela, width=400, height=1, background="grey")
line3.place(x=35, y=310)

button2 = Button(janela, text='Submit!', command=bt_click).place(x=210, y=370)

###############################
#Size window and position
janela.geometry("480x450+300+300")
janela.mainloop()
