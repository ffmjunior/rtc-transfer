#!/usr/bin/env python.exe
"""
<a href="https://www.flaticon.com/free-icons/exchange" title="exchange icons">Exchange icons created by Freepik - Flaticon</a>
"""

import pystray

from PIL import Image, ImageDraw
from pystray import MenuItem as item
from tkinter.filedialog import askopenfilename, asksaveasfilename

class UI:

    def __init__(self) -> None:
        self.image = Image.open("resources\exchange.png")
        self.menu=( item('Send File', self.show_file_dialog), item('Receive File', self.show_save_dialog), item('Quit', self.quit_window))
        self.icon=pystray.Icon("name", self.image, "My System Tray Icon", self.menu)
        self.icon.run()


    # Define  function for quit the window
    def quit_window(self, icon, item):
        self.icon.stop()

    # Define a function to show the window again
    def show_file_dialog(self, icon, item):
        self.filename = askopenfilename()
        return self.filename

    def show_save_dialog(self, icon, item):
        self.filename = asksaveasfilename()
        return self.filename





ui = UI()
