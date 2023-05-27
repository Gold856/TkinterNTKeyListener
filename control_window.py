import tkinter as tk
from tkinter import *

from networktables import NetworkTable, NetworkTables
from pynput import keyboard

# Initialize NetworkTables and get the SmartDashboard table
NetworkTables.initialize(server='10.0.20.2')
NetworkTables.startDSClient()
table: NetworkTable = NetworkTables.getTable('SmartDashboard')
table.putBoolean("NUMPAD1", False)
table.putBoolean("NUMPAD2", False)
table.putBoolean("NUMPAD3", False)
table.putBoolean("NUMPAD4", False)
table.putBoolean("NUMPAD5", False)
table.putBoolean("NUMPAD6", False)
table.putBoolean("NUMPAD7", False)
table.putBoolean("NUMPAD8", False)
table.putBoolean("NUMPAD9", False)

# setup tkinter (width of the screen)
root = tk.Tk()
root.geometry(str(root.winfo_screenwidth())+"x400-1+" + str(0))
c = tk.Canvas(root)
frame = Frame(root)




class KeyboardButton(Button):
    """ A modified button that flashes green when active""" 
    button_width = 10
    button_height = 5
    button_pressed_color = "lime"

    def __init__(self, text: str = None) -> None:
        super().__init__(frame, text=text, width=self.button_width,
                         height=self.button_height, activebackground=self.button_pressed_color)


def key_down(event: keyboard.KeyCode):
    if type(event) == keyboard.KeyCode:
        # Check to make sure the keys come from the numpad
        match event.vk:
            case 97:
                numpad1_button.configure(state="active")
                table.putBoolean("NUMPAD1", True)
            case 98:
                numpad2_button.configure(state="active")
                table.putBoolean("NUMPAD2", True)
            case 99:
                numpad3_button.configure(state="active")
                table.putBoolean("NUMPAD3", True)
            case 100:
                numpad4_button.configure(state="active")
                table.putBoolean("NUMPAD4", True)
            case 101:
                numpad5_button.configure(state="active")
                table.putBoolean("NUMPAD5", True)
            case 102:
                numpad6_button.configure(state="active")
                table.putBoolean("NUMPAD6", True)
            case 103:
                numpad7_button.configure(state="active")
                table.putBoolean("NUMPAD7", True)
            case 104:
                numpad8_button.configure(state="active")
                table.putBoolean("NUMPAD8", True)
            case 105:
                numpad9_button.configure(state="active")
                table.putBoolean("NUMPAD9", True)
            case 109:
                minus_button.configure(state="active")
                table.putBoolean("-", True)
            case 107:
                plus_button.configure(state="active")
                table.putBoolean("+", True)


def key_up(event: keyboard.KeyCode):
    if type(event) == keyboard.KeyCode:
        # Check to make sure the keys come from the numpad
        match event.vk:
            case 97:
                numpad1_button.configure(state="normal")
                table.putBoolean("NUMPAD1", False)
            case 98:
                numpad2_button.configure(state="normal")
                table.putBoolean("NUMPAD2", False)
            case 99:
                numpad3_button.configure(state="normal")
                table.putBoolean("NUMPAD3", False)
            case 100:
                numpad4_button.configure(state="normal")
                table.putBoolean("NUMPAD4", False)
            case 101:
                numpad5_button.configure(state="normal")
                table.putBoolean("NUMPAD5", False)
            case 102:
                numpad6_button.configure(state="normal")
                table.putBoolean("NUMPAD6", False)
            case 103:
                numpad7_button.configure(state="normal")
                table.putBoolean("NUMPAD7", False)
            case 104:
                numpad8_button.configure(state="normal")
                table.putBoolean("NUMPAD8", False)
            case 105:
                numpad9_button.configure(state="normal")
                table.putBoolean("NUMPAD9", False)
            case 109:
                minus_button.configure(state="normal")
                table.putBoolean("-", False)
            case 107:
                plus_button.configure(state="normal")
                table.putBoolean("+", False)


# Create the keyboard buttons
numpad1_button = KeyboardButton(text="NUMPAD1")
numpad2_button = KeyboardButton(text="NUMPAD2")
numpad3_button = KeyboardButton(text="NUMPAD3")
numpad4_button = KeyboardButton(text="NUMPAD4")
numpad5_button = KeyboardButton(text="NUMPAD5")
numpad6_button = KeyboardButton(text="NUMPAD6")
numpad7_button = KeyboardButton(text="NUMPAD7")
numpad8_button = KeyboardButton(text="NUMPAD8")
numpad9_button = KeyboardButton(text="NUMPAD9")
minus_button = KeyboardButton(text="-")
plus_button = KeyboardButton(text="+")
# Place the buttons on the grid
numpad1_button.grid(row=2, column=0, padx=20, pady=20)
numpad2_button.grid(row=2, column=1, padx=20, pady=20)
numpad3_button.grid(row=2, column=2, padx=20, pady=20)
numpad4_button.grid(row=1, column=0, padx=20, pady=20)
numpad5_button.grid(row=1, column=1, padx=20, pady=20)
numpad6_button.grid(row=1, column=2, padx=20, pady=20)
numpad7_button.grid(row=0, column=0, padx=20, pady=20)
numpad8_button.grid(row=0, column=1, padx=20, pady=20)
numpad9_button.grid(row=0, column=2, padx=20, pady=20)
minus_button.grid(row=0, column=4, padx=20, pady=20)
plus_button.grid(row=1, column=4, padx=20, pady=20)
# Center everything
frame.place(relx=0.5, rely=0.5, anchor=CENTER)
# Activate keyboard listeners
keyboard_listener = keyboard.Listener(on_press=key_down, on_release=key_up)
keyboard_listener.start()
# GO!!
root.mainloop()
