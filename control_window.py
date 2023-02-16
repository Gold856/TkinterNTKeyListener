import tkinter as tk
from tkinter import *

from networktables import NetworkTables
from pynput import keyboard

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
    button_pressed_color = "lime"

    def __init__(self, text: str = None) -> None:
        super().__init__(frame, text=text, width=self.button_width,
                         height=self.button_height, activebackground=self.button_pressed_color)


def key_down(event: keyboard.KeyCode):
    if type(event) == keyboard.KeyCode:
        print(event.vk)
        # Check to make sure the keys come from the numpad
        match event.vk:
            case 97:
                numpad1_button.configure(state="active")
            case 98:
                numpad2_button.configure(state="active")
            case 99:
                numpad3_button.configure(state="active")
            case 100:
                numpad4_button.configure(state="active")
            case 101:
                numpad5_button.configure(state="active")
            case 102:
                numpad6_button.configure(state="active")
            case 103:
                numpad7_button.configure(state="active")
            case 104:
                numpad8_button.configure(state="active")
            case 105:
                numpad9_button.configure(state="active")
            case 109:
                minus_button.configure(state="active")
            case 107:
                plus_button.configure(state="active")


def key_up(event: keyboard.KeyCode):
    if type(event) == keyboard.KeyCode:
        # Check to make sure the keys come from the numpad
        match event.vk:
            case 97:
                numpad1_button.configure(state="normal")
            case 98:
                numpad2_button.configure(state="normal")
            case 99:
                numpad3_button.configure(state="normal")
            case 100:
                numpad4_button.configure(state="normal")
            case 101:
                numpad5_button.configure(state="normal")
            case 102:
                numpad6_button.configure(state="normal")
            case 103:
                numpad7_button.configure(state="normal")
            case 104:
                numpad8_button.configure(state="normal")
            case 105:
                numpad9_button.configure(state="normal")
            case 109:
                minus_button.configure(state="normal")
            case 107:
                plus_button.configure(state="normal")


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
frame.place(relx=0.5, rely=0.5, anchor=CENTER)
keyboard_listener = keyboard.Listener(on_press=key_down, on_release=key_up)
keyboard_listener.start()
root.mainloop()
