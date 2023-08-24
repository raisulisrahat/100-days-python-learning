# Here I showing GUI in python part 3

from tkinter import *
from tkinter.ttk import *
from time import strftime
import calendar  # Import the correct module

root = Tk()
root.title("Clock and Calendar")

class window(Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack()
        self.create_widgets()  # Call the widget creation function

    def create_widgets(self):
        self.clock_label = Label(self, font=('calibri', 40, 'bold'), background='purple', foreground='white')
        self.clock_label.pack(anchor='center')

        self.date_label = Label(self, font=('calibri', 20, 'bold'), background='blue', foreground='white')
        self.date_label.pack(anchor='center')

        self.update_time()  # Start updating time immediately
        self.update_date()  # Start updating date immediately

    def update_time(self):
        string = strftime('%H:%M:%S %p')
        self.clock_label.config(text=string)
        self.after(1000, self.update_time)  # Update every 1000ms (1 second)

    def update_date(self):
        year = 2023  # Change this to the desired year
        month = 8    # Change this to the desired month
        cal_text = calendar.month(year, month)
        self.date_label.config(text=cal_text)
        
# Create an instance of the window class
app = window(root)

# Run the main loop
root.mainloop()



