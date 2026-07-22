# Author: mm no
# Date: time is js a concept
# Purpose: making the design

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
s = ttk.Style()
s.configure('mainFrame.TFrame', background = '#FEFFFE')

s.configure('Lable.TLabel', background = '#D5C7BC') # diff colour so can tell 
mainFrame = ttk.Frame(root, width = 250, height= 250, style= 'mainFrame.TFrame')
mainFrame.grid()

Home = ttk.Label(mainFrame, text = "Home", style= 'Lable.TLabel')
Home.grid(row=0, column = 0, padx = 15, pady = 15, sticky = 'N')
root.resizable(width = False, height = False)
root.mainloop()

#ok so this works
