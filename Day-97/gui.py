# here i am showing DevOps project Day 7

import tkinter as tk
from tkinter import messagebox

def deploy():
    # Add deployment logic here
    messagebox.showinfo("Deployment", "Deployment initiated")

def scale():
    # Add scaling logic here
    messagebox.showinfo("Scaling", "Scaling initiated")

def monitor():
    # Add monitoring logic here
    messagebox.showinfo("Monitoring", "Monitoring initiated")

def main():
    root = tk.Tk()
    root.title("DevOps Tool")

    deploy_button = tk.Button(root, text="Deploy", command=deploy)
    deploy_button.pack()

    scale_button = tk.Button(root, text="Scale", command=scale)
    scale_button.pack()

    monitor_button = tk.Button(root, text="Monitor", command=monitor)
    monitor_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
