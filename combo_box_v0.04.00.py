# Author: mm no
# Date: time is js a concept
# Purpose: making the design

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
#def
def selection():
    label.config(text=f"Selected: {variable.get()}")
variable = tk.StringVar(root, f"{options[0]}")
#Style
s = ttk.Style()
s.configure('mainFrame.TFrame', background = '#FFFFFF')
s.configure('Frame2.TFrame', background = '#D5C7BC')
s.configure('Frame3.TFrame', background = '#E9FAE4')
s.configure('Frame4.TFrame', background = '#DEE8D6')
s.configure('Lable.TLabel', background = '#DEE8D6', font = ('Helvetica, 14')) 
#Frames
mainFrame = ttk.Frame(root, width = 250, height= 250, style= 'mainFrame.TFrame')
mainFrame.grid()
Frame2 = ttk.Frame(root, width =250, height = 50, style= 'Frame2.TFrame')
Frame2.grid()
Frame3 = ttk.Frame(root, width =250, height = 35, style= 'Frame3.TFrame')
Frame3.grid(row =0, column = 0, sticky = 'N')
Frame4 = ttk.Frame(root, width =62.5, height = 35, style= 'Frame4.TFrame')
Frame4.grid(row =0, column = 0, sticky = 'NW')
Home = ttk.Label(Frame4, text = "Home", style= 'Lable.TLabel')
Home.grid(row=0, column = 0, padx = 15, pady = 4.4, sticky = 'N')
label = tk.Label(root,text=f"Selected: {options[0]}")
label.grid(row=0, column=0, padx=10, pady=10, sticky="NE")

#button?
button = tk.Button(root, width =9, height = 5, bg='#DEE8D6', text="button")
button.grid(row=0, column=0, padx = 15, sticky = 'W')
#combo box?
for option in options:
    tk.Radiobutton(
        root,
        text=option,
        variable=variable,
        value=option,
        command=selection,
        ).grid(padx = 10, pady=5)

root.resizable(width = False, height = False)
root.mainloop()

#combo box
