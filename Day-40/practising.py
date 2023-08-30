# Here I am showing python Web status checker with requests modules

import requests
import tkinter as tk
from tkinter import messagebox

def check_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "is up"
        else:
            return f"is down with status code {response.status_code}"
    except requests.RequestException:
        return "could not be reached"

def check_button_click():
    urls = url_text.get("1.0", "end-1c").splitlines()
    
    if not urls:
        messagebox.showwarning("No URLs", "Please enter at least one URL.")
        return
    
    results_text.delete("1.0", "end")
    
    for url in urls:
        status = check_status(url)
        results_text.insert("end", f"{url} {status}\n")
    
    results_text.see("end")

# Create the main window
root = tk.Tk()
root.title("Website Status Checker")

# Create and pack GUI components
url_label = tk.Label(root, text="Enter URLs (one per line):")
url_label.pack()

url_text = tk.Text(root, height=5, width=40)
url_text.pack()

check_button = tk.Button(root, text="Check Status", command=check_button_click)
check_button.pack()

results_label = tk.Label(root, text="Results:")
results_label.pack()

results_text = tk.Text(root, height=10, width=40)
results_text.pack()

root.mainloop()
