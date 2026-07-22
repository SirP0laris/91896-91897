# Author: mm no
# Date: June 3rd 2026
# Purpose: Create a greeting app

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
s = ttk.Style()
s.configure('mainFrame.TFrame', background = '#FEFFFE')
s.configure('Frame2.TFrame', background = '#A5A299')
s.configure('Frame3.TFrame', background = '#E9EBF8')
s.configure('Frame4.TFrame', background = '#E9EBF8')
mainFrame = ttk.Frame(root, width = 250, height= 250, style= 'mainFrame.TFrame')
mainFrame.grid()
Frame2 = ttk.Frame(root, width =250, height = 50, style= 'Frame2.TFrame')
Frame2.grid()
Frame3 = ttk.Frame(root, width =250, height = 35, style= 'Frame3.TFrame')
Frame3.grid(row =0, column = 0, sticky = 'N')
Frame4 = ttk.Frame(root, width =60, height = 35, style= 'Frame4.TFrame')
Frame4.grid(row =0, column = 0, sticky = 'NW')
root.resizable(width = False, height = False)
root.mainloop()
