#!/usr/bin/env python3


import tkinter

class Example:

    def __init__(self):
        #super().__init__()

        self.initUI()
        
        
    def initUI(self):
        # Title the window
        #self.master.title("Guessing Game")
        #self.pack(fill=BOTH, expand=True)

        # create main window
        self.frame1 = tkinter.Frame(self)
        self.frame1.pack(fill=X)

        # Display first label
        self.lbl1 = tkinter.Label(frame1, text="     Guess a number between 1 and 100     ")
        self.lbl1.pack(fill=X)

        # put that to the frame and make it the width of the window
        self.frame2 = tkinter.Frame(self)
        self.frame2.pack(fill=X)

        # display second label
        self.lbl2 = tkinter.Label(frame2, text="Your Guess: ", width=15)
        self.lbl2.pack(side=LEFT, padx=5, pady=5)

        # provide guessing box
        self.entry = tkinter.StringVar()
        self.enter = tkinter.Entry(frame2, textvariable=self.entry)
        self.enter.pack(fill=X, padx=5, expand=True)

        # make sure buttons are at the bottom
        self.frame3 = tkinter.Frame(self)
        self.frame3.pack(fill=BOTH, expand=True)

        def on_button(self):
            if entry.get() == "42":
                self.slabel = tkinter.Label(self, text="You guessed right!")
                self.slabel.pack()
            else:
                self.tlabel = tkinter.Label(self, text="")
                self.tlabel.pack()

        # Next Button
        self.obtn = tkinter.Button(self, text="Next", command=on_button(self))
        self.obtn.pack(side=LEFT)

        # New Game Button
        self.hbtn = tkinter.Button(self, text="New Game")
        self.hbtn.pack(side=RIGHT)
        


def main():

    app = Example()
    tkinter.mainloop()



if __name__ == '__main__':
    main()
