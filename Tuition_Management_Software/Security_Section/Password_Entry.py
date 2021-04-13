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
    entry.focus_set()
    
    def legal_exit():
        import os
        os._exit(0)
        
    b1=ttk.Button(pass_win, text='Exit', command=legal_exit)
    b1.grid(row=2,column=1, padx=5, pady=5)

    # code to disable exit button
    pass_win.protocol("WM_DELETE_WINDOW", disable_event)

    def dynamic_checking():

        print('Waiting...')
        time.sleep(1) # So as to avoid max recursion depth 
        print('Checking')

        if entry.get() != 'abcdef': # checking entry box's text after each sec
            entry['bg']='red'
            entry['fg']='white'
            dynamic_checking()

        else:
            entry['bg']='blue'
            pass_win.destroy()
            print('Correct password detected')

    threading.Thread(target=dynamic_checking).start()
    pass_win.mainloop()
