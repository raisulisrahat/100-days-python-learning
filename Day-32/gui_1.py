# Here i showing python GUI part 1
from tkinter import *
from tkinter import ttk

root = Tk()
ui = ttk.Frame(root, padding=100)
ui.grid()
ttk.Label(ui, text="Hi I am Rahat.").grid(column=0, row=0)
ttk.Button(ui, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

