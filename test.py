
from tkinter import *
def getinfo():
    print(e1.get())
    print(e2.get())
master = Tk()
master.title = "Test"
master.geometry('300x100')
Label(master, text="username").grid(row=0)
Label(master, text="password").grid(row=1)

e1 = Entry(master)
e2 = Entry(master,show="*")

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

Button(master,text="set",command=getinfo).grid(row=2,column=1)

mainloop()
