#! /usr/bin/env python3

import tkinter

class GuessIt:
    def __init__(self):
        # main window
        self.main_window = tkinter.Tk()

        # make the frames
        self.guess_frame = tkinter.Frame(self.main_window)
        self.your_guess_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # make your guess title
        self.guess_label = tkinter.Label(self.main_window, text='     Guess a number between 1 and 100     ')
        self.guess_label.pack(fill='x')

        # enter your guess
        self.your_guess_label = tkinter.Label(self.main_window, text='     Your guess:')
        self.your_guess_entry = tkinter.Entry(self.your_guess_frame, width=15)
        self.your_guess_label.pack(side='left')
        self.your_guess_entry.pack(side='right')

        # make the buttons
        self.new_game_button = tkinter.Button(self.button_frame, text='New Game')
        self.next_button = tkinter.Button(self.button_frame, text='Next')
        self.new_game_button.pack(side='right')
        self.next_button.pack(side='left')

        # pack them all
        self.guess_frame.pack()
        self.your_guess_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

guess_it = GuessIt()
