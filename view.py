# These are imported and are packaged from tkinter #@7.15mins
import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    
    def __init__(self,controller):
        self.controller = controller

        # This essentially helps us with inheritance from tkinter.
        super().__init__()

    def main(self):
        # This is an infinite loop for tkinter
        self.mainloop()
