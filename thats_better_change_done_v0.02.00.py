# Author: mm no
# Date: time is js a concept
# Purpose: making the design

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
#Style
s = ttk.Style()
s.configure('mainFrame.TFrame', background = '#FEFFFE')
s.configure('Frame2.TFrame', background = '#A5A299')
s.configure('Frame3.TFrame', background = '#E9EBF8')
s.configure('Frame4.TFrame', background = '#B4B8C5')
s.configure('Lable.TLabel', background = '#B4B8C5', font = ('Helvetica, 14')) 
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
root.resizable(width = False, height = False)
root.mainloop()

#ok so i did it
