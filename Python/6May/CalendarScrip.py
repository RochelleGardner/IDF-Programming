import tkinter as tk
import calendar
import time
from tkinter import ttk



def sequence(*functions):  # to run 2 or more functions on button click
    for function in functions:
        function()


def update(y, m, tx, curdate):  # generate calendar with right colors
    calstr = calendar.month(y, m)
    tx.configure(state=tk.NORMAL)
    tx.delete('0.0', tk.END)  # remove previous calendar
    tx.insert(tk.INSERT, calstr)
    for i in range(2, 9):
        tx.tag_add("others", '{}.0'.format(i), '{}.end'.format(i))  # tag days for coloring
        if len(tx.get('{}.0'.format(i), '{}.end'.format(i))) == 20:
            tx.tag_add("sun", '{}.end-2c'.format(i), '{}.end'.format(i))
    tx.tag_config("sun", foreground="#bc00ff")
    tx.tag_config("others", foreground="#ff0000")
    tx.tag_add("head", '1.0', '1.end')
    if curdate[0] == y and curdate[1] == m:
        index = tx.search(str(curdate[2]), '2.0')  # search for today's date
        tx.tag_add("cur", index, '{}+2c'.format(index))  # highlight today's date
        tx.tag_config("cur", background="black", foreground="#ff0090")
    tx.tag_config("head", foreground="#0d8241", justify=tk.CENTER)
    tx.configure(state=tk.DISABLED)  # make text view not editable


top = tk.Tk()
top.title("Calendar")
top.minsize(200, 200)
top.maxsize(250, 250)
#font = Font(family = "Segoe UI")
logo = tk.PhotoImage(file="Britalstar.gif")
top.tk.call('wm', 'iconphoto', top._w, logo)

curtime = time.localtime()
year = tk.StringVar()
month = tk.StringVar()
yearInt = curtime[0]
monthInt = curtime[1]
dateInt = curtime[2]
HLayout = ttk.PanedWindow(top, orient=tk.HORIZONTAL)
ctx = tk.Text(top, padx=10, pady=10, bg="#beff00", relief=tk.FLAT, height=9,
                   width=20)  # text view to passing to functions


def nextb():  # on click next button
    global monthInt, yearInt, ctx, curtime
    monthInt += 1
    if monthInt > 12:
        monthInt = monthInt % 12
        yearInt += 1
    update(yearInt, monthInt, ctx, curtime)


def prevb():  # on click previous button
    global monthInt, yearInt, ctx, curtime
    monthInt -= 1
    if monthInt < 1:
        monthInt = 12
        yearInt -= 1
    update(yearInt, monthInt, ctx, curtime)


def okcall():  # ok button click inside go to date window
    global monthInt, yearInt, ctx, curtime
    if (year.get().isdigit() and month.get().isdigit()) and (
                (0 < int(year.get()) < 10000) and (0 < int(month.get()) < 13)):
        yearInt = int(year.get())
        monthInt = int(month.get())
        update(yearInt, monthInt, ctx, curtime)


def gotod():  # go to date window creation
    newtop = tk.Toplevel()
    newtop.title("Calendar")
    newtop.maxsize(190, 190)
    newtop.focus_set()
    newtop.tk.call('wm', 'iconphoto', newtop._w, logo)
    HLayout = ttk.PanedWindow(newtop, orient=tk.HORIZONTAL)
    HLayout2 = ttk.PanedWindow(newtop, orient=tk.HORIZONTAL)
    yearText = ttk.Label(HLayout, text="Year :")
    yearEdit = ttk.Entry(HLayout, textvariable=year)
    monthText = ttk.Label(HLayout2, text="Month:")
    monthEdit = ttk.Entry(HLayout2, textvariable=month)
    okb = ttk.Button(newtop, text="Ok", command=lambda: sequence(okcall, newtop.destroy))
    yearText.pack(side=tk.LEFT)
    yearEdit.pack(side=tk.RIGHT)
    monthText.pack(side=tk.LEFT)
    monthEdit.pack(side=tk.RIGHT)
    HLayout.pack()
    HLayout2.pack()
    okb.pack()
    newtop.mainloop()


def about_show():  # about window creation
    newtop = tk.Toplevel()
    newtop.title("Calendar")
    newtop.maxsize(190, 190)
    newtop.focus_set()
    newtop.tk.call('wm', 'iconphoto', newtop._w, logo)
    about = ttk.LabelFrame(newtop, text="About")
    tk.Label(about, text="Calendar 2.0").pack()
    tk.Label(about, image=logo, text="Developer: Britalstar", compound=tk.BOTTOM).pack()
    about.pack()
    newtop.mainloop()


update(yearInt, monthInt, ctx, curtime)  # for first run, generate calendar
prev = ttk.Button(HLayout, text="<<", command=prevb)
nex = ttk.Button(HLayout, text=">>", command=nextb)
goto = ttk.Button(top, text="Goto", command=gotod)
menubar = tk.Menu(top, relief=tk.FLAT)
filemenu = tk.Menu(menubar, tearoff=0, relief=tk.FLAT)
helpmenu = tk.Menu(menubar, tearoff=0, relief=tk.FLAT)
filemenu.add_command(label="Goto", command=gotod)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.destroy)
helpmenu.add_command(label="About", command=about_show)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Help", menu=helpmenu)
top.config(menu=menubar)
prev.pack(side=tk.LEFT)
nex.pack(side=tk.RIGHT)
ctx.pack()
HLayout.pack()
goto.pack()
top.mainloop()