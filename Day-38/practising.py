# Here I showing python base Scientific Calculator

from tkinter import *
from tkinter.ttk import *

class Calculator(Frame):
    def __init__(self, gui):
        super().__init__(gui)
        self.gui = gui
        self.gui.configure(background="light blue")
        self.gui.title("GUI Calculator")
        self.gui.geometry("340x240")
        self.equation = StringVar()
        self.expression_field = Entry(self.gui, textvariable=self.equation)
        self.expression_field.grid(column=4, ipadx=70)

        self.style = Style()
        self.style.configure("TButton", foreground="black", background="red")

        self.create_buttons()

    def press(self, num):
        ex = self.equation.get() + str(num)
        self.equation.set(ex)

    def equalpress(self):
        try:
            total = str(eval(self.equation.get()))
            self.equation.set(total)
        except:
            self.equation.set("error")

    def clear(self):
        self.equation.set("")

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 2
        col = 0
        for button in buttons:
            if button == '=':
                btn = Button(self.gui, text=button, command=self.equalpress)
            else:
                btn = Button(self.gui, text=button, command=lambda b=button: self.press(b))

            btn.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1


if __name__ == "__main__":
    gui = Tk()
    app = Calculator(gui)
    gui.mainloop()




        