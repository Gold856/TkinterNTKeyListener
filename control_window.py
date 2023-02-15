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


class KeyboardButton(Button):
    button_width = 10
    button_height = 5

    def __init__(self, text: str = None) -> None:
        super().__init__(frame, text=text, width=self.button_width, height=self.button_height)


numpad1_button = KeyboardButton(text="NUMPAD1")
numpad2_button = KeyboardButton(text="NUMPAD2")
numpad3_button = KeyboardButton(text="NUMPAD3")
numpad4_button = KeyboardButton(text="NUMPAD4")
numpad5_button = KeyboardButton(text="NUMPAD5")
numpad6_button = KeyboardButton(text="NUMPAD6")
numpad7_button = KeyboardButton(text="NUMPAD7")
numpad8_button = KeyboardButton(text="NUMPAD8")
numpad9_button = KeyboardButton(text="NUMPAD9")
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
root.mainloop()
