#!/usr/bin/env python.exe
"""
<a href="https://www.flaticon.com/free-icons/exchange" title="exchange icons">Exchange icons created by Freepik - Flaticon</a>
"""

import pystray

from PIL import Image, ImageDraw
from pystray import MenuItem as item
from tkinter import Tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename

class UI:

    def __init__(self) -> None:
        pass

    def read_file(self) -> str:
        pass

    def save_file(self) -> str:
        pass


class CLI(UI):
    def read_file(self) -> str:
        return super().read_file()

    def save_file(self) -> str:
        return super().save_file()


class GUI(UI):
    def __init__(self) -> None:
        Tk().withdraw()
        self.image = Image.open("resources\exchange.png")
        self.menu=( item('Send File', self.read_file), item('Receive File', self.save_file), item('Quit', self.quit_window))
        self.icon=pystray.Icon("name", self.image, "My System Tray Icon", self.menu)
        self.icon.run()


    # Define  function for quit the window
    def quit_window(self):
        self.icon.stop()

    # Define a function to show the window again
    def read_file(self):
        self.filename = askopenfilename()
        return str(self.filename)

    def save_file(self):
        self.filename = asksaveasfilename()
        return str(self.filename)


ui = GUI()
