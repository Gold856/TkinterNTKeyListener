import tkinter as tk
from tkinter import *

import keyboard
from networktables import NetworkTables

# intialize network tables and get the smart dashboard
NetworkTables.initialize(server='10.0.20.2')
sd = NetworkTables.getTable('SmartDashboard')

# setup tkinter (width of the screen, 100 px tall)
root = tk.Tk()
root.geometry(str(root.winfo_screenwidth())+"x400-1+" + str(0))
c = tk.Canvas(root)
frame = Frame(root)
bWidth = 10
bHeight = 5

numpad1_button = Button(frame, text="NUMPAD1", width=bWidth, height=bHeight)
numpad2_button = Button(frame, text="NUMPAD2", width=bWidth, height=bHeight)
numpad3_button = Button(frame, text="NUMPAD3", width=bWidth, height=bHeight)
numpad4_button = Button(frame, text="NUMPAD4", width=bWidth, height=bHeight)
numpad5_button = Button(frame, text="NUMPAD5", width=bWidth, height=bHeight)
numpad6_button = Button(frame, text="NUMPAD6", width=bWidth, height=bHeight)
numpad7_button = Button(frame, text="NUMPAD7", width=bWidth, height=bHeight)
numpad8_button = Button(frame, text="NUMPAD8", width=bWidth, height=bHeight)
numpad9_button = Button(frame, text="NUMPAD9", width=bWidth, height=bHeight)
numpad1_button.grid(row=2, column=0, padx=20, pady=20)
numpad2_button.grid(row=2, column=1, padx=20, pady=20)
numpad3_button.grid(row=2, column=2, padx=20, pady=20)
numpad4_button.grid(row=1, column=0, padx=20, pady=20)
numpad5_button.grid(row=1, column=1, padx=20, pady=20)
numpad6_button.grid(row=1, column=2, padx=20, pady=20)
numpad7_button.grid(row=0, column=0, padx=20, pady=20)
numpad8_button.grid(row=0, column=1, padx=20, pady=20)
numpad9_button.grid(row=0, column=2, padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)


def update():
    # Get values from network tables
    # run every 100 milliseconds
    root.after(100, update)


# start sensor update loop
update()
keyboard.on_press_key
root.mainloop()
