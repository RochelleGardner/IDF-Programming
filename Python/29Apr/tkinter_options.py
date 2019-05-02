#!/usr/bin/env python3


from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT
from tkinter.ttk import Frame, Label, Entry, Button

class WindowGUI:
    def __init__(self):
            
            
    def doTheMath(self):
        number = 42
        looping = True
        guess_count = 0

        while looping == True:
            if number < 1:
                print ("Please try with a number greater than 1...")
            elif number > 100:
                print ("Please try with a number 100 or less...")
            elif number < 42 and number > 0:
                print ("Your guess was too low...")
                guess_count = guess_count + 1
            elif number > 42 and number < 101:
                print ("Your guess was too high...")
                guess_count = guess_count + 1
            elif number == 42:
                print ("You got it in ", guess_count, " guesses!")
                looping = False
            else:
                print ("That isn't even an option...")