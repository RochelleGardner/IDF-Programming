#! /usr/bin/env python3

import tkinter

class Colors:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.color1 = tkinter.Label(self.main_window, text='RED', fg="red", bg='green',width=20)
        self.color2 = tkinter.Label(self.main_window, text='WHITE', fg="white", bg='green',width=20)
        self.color3 = tkinter.Label(self.main_window, text='BLUE', fg="blue", bg='green',width=20)

        self.color1.pack()
        self.color2.pack()
        self.color3.pack()

        tkinter.mainloop()

color = Colors()
