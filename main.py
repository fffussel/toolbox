from tkinter import *
from tkinter import ttk
import os


moduleDir = "./modules"
files = [f for f in os.listdir(moduleDir) if f.endswith(".py")]
root = Tk()


def open(filename:str):
    global moduleDir 
    global root

    if not moduleDir.endswith("/"):
        moduleDir = moduleDir + "/"
    os.system("python " + moduleDir + filename)
    root.destroy()


root.title("Toolbox")
frm = ttk.Frame(root, padding=20)
frm.grid()

i = 0

for file in files:

    button = ttk.Button(
    frm,
    text=file.removesuffix(".py"),
    command=lambda f=file: open(f)
    )
    button.config(width=40)
    button.grid(column=0, row=i)


    i += 1

root.mainloop()