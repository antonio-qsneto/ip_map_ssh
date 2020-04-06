from tkinter import *
from functools import partial
from tkinter import filedialog

janela = Tk()

janela.title("Ip Map SSH")

header = Label(janela, text="Ip Map SSH", background="blue")
header.place(x=200, y=40)

##############Labels##############
lb1 = Label(janela, text="IP:")
lb1.place(x=50, y=100)
ed1 = Entry(janela)
ed1.place(x=90, y=100)


lb2 = Label(janela, text="Port:")
lb2.place(x=240, y=100)
ed2 = Entry(janela)
ed2.place(x=300, y=100)

lb3 = Label(janela, text="Login:")
lb3.place(x=50, y=140)
ed3 = Entry(janela)
ed3.place(x=90, y=140)

lb4 = Label(janela, text="Password:")
lb4.place(x=240, y=140)
ed4 = Entry(janela)
ed4.place(x=300, y=140)

###########################################
line1 = Canvas(janela, width=400, height=1, background="grey")
line1.place(x=35, y=180)

lb5 = Label(janela, text="Command Shell:")
lb5.place(x=50, y=210)
ed5 = Entry(janela)
ed5.place(x=140, y=210, width=287)
###########################################


line2 = Canvas(janela, width=400, height=1, background="grey")
line2.place(x=35, y=250)

lb6 = Label(janela, text="File Brutal force:")
lb6.place(x=50, y=280)

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

button = Button(janela, text='File.txt', command=UploadAction).place(x=180, y=275)
#button.pack()

line3 = Canvas(janela, width=400, height=1, background="grey")
line3.place(x=35, y=310)

button2 = Button(janela, text='Submit!', command=None).place(x=210, y=370)

###############################
#Size window and position
janela.geometry("480x450+300+300")
janela.mainloop()
