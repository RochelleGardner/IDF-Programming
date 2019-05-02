#! /usr/bin/env python3

import tkinter as tk
from tkinter import ttk

class CounterProgram:

    def __init__(self):
        self.window = tk.Tk()
        self.guess_counter = None  # All attributes should be initialize in init
        self.create_widgets()

    def create_widgets(self):
        self.guess_counter = ttk.Label(self.window, text="0")
        self.guess_counter.grid(row=0, column=0)

        increment_button = ttk.Button(self.window, text="Next")
        increment_button.grid(row=1, column=0)
        increment_button['command'] = self.increment_counter

        quit_button = ttk.Button(self.window, text="New Game")
        quit_button.grid(row=2, column=0)
        quit_button['command'] = self.window.destroy

    def increment_counter(self):
        self.guess_counter['text'] = str(int(self.guess_counter['text']) + 1)

# Create the entire GUI program
program = CounterProgram()

# Start the GUI event loop
program.window.mainloop()