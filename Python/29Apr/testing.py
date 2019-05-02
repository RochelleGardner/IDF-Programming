#! /usr/bin/env python3

from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT
from tkinter.ttk import Frame, Label, Entry, Button


root = Tk()
root.geometry("300x300+300+300")
root.title("Guessing Game")

entry = Entry(root)
entry.pack()

# make sure buttons are at the bottom
frame3 = Frame(root)
frame3.pack(fill=BOTH, expand=True)

# New Game Button
hbtn = Button(root, text="New Game")
hbtn.pack(side=RIGHT)

# Next Button
obtn = Button(root, text="Next")
obtn.pack(side=LEFT)

def on_button():
    if entry.get() == "42":
        slabel = Label(root, text="You guessed right!")
        slabel.pack()
    else:
        tlabel = Label(root, text="")
        tlabel.pack()

button = Button(root, text="Enter", command=on_button)
button.pack()

root.mainloop()
