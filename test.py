
from tkinter import *

master = Tk()

Label(master, text="username").grid(row=0)
Label(master, text="password").grid(row=1)

e1 = Entry(master)
e2 = Entry(master,show="*")

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
print('test')
mainloop()
