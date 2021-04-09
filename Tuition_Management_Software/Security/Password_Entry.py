# This program is made in order to verify that no unwanted person is running this program with the by putting a password check

# Importing necessary libraries
from tkinter import *
from tkinter import ttk
from Classes import *
import threading
import time


def password():

    def disable_event():
        pass

    pass_win = Tk()
    pass_win_gui = window(pass_win, 'Password')

    entry = Entry(pass_win, bd=10, font=('georgia', 25), show='*')
    entry.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    # code to disable exit button
    pass_win.protocol("WM_DELETE_WINDOW", disable_event)

    def dynamic_checking():

        print('Waiting...')
        time.sleep(1)
        print('Checking')

        if entry.get() != 'abcd':
            dynamic_checking()

        else:

            pass_win.destroy()
            print('Correct password detected')

    threading.Thread(target=dynamic_checking).start()
    pass_win.mainloop()
