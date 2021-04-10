# Python file containing program to analyse registration records

# Importing necessary libraries
from Classes import *
from tkinter import *
from tkinter import ttk
import threading
import win32api
import pyttsx3
import time

lock = threading.Lock()


def speak(text, lock=lock):
    def process(text, lock):  # In case any user operates program very fast and clicks records submit button , then an error can take place as no time.sleep has been put therefore if something is being spoken , then a runtime error can take place
        print('Sleeping for 2 sec...')
        time.sleep(2)
        print('Woken sir ,feeling fresh now')
        lock.acquire()
        pyttsx3.speak(text)
        lock.release()

    threading.Thread(target=process, args=(text, lock)).start()


def imports():
    global Calendar, DateEntry, datetime, pd, plt, string, os, pywhatkit
    from tkcalendar import Calendar, DateEntry
    print('Calendar, DateEntry imported')
    from datetime import datetime
    print('Datetime imported')
    import pandas as pd
    print('Pandas imported')
    import matplotlib.pyplot as plt
    print('Matplotlib imported')
    import string
    print('String imported')
    import os
    print('OS imported')
    import pywhatkit
    print('Pywhatkit imported')


threading.Thread(target=imports).start()


def registration_analysis():

    # Preparing window for analysis

    print('Preparing window for registration analysis...')
    reg_anal_win = Tk()
    reg_anal_win_gui = window(reg_anal_win, 'Registration Analysis')

    reg_anal_win_lf1 = LabelFrame(reg_anal_win, text='Analysis Section')
    reg_anal_win_lf1.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    # Asking for the type of analysis user wants
    
    # Monthly analysis button program
    
    def reg_anal_b1_func():
        
        speak('Performing Monthly Analysis sir')

    reg_anal_b1 = ttk.Button(
        reg_anal_win_lf1, text='Monthly Analysis', command=reg_anal_b1_func)
    reg_anal_b1.grid(row=0, column=0, padx=10, pady=10)
    
    # Classwise analysis button program
    
    def reg_anal_b2_func():
        
        speak('Performing classwise analysis sir')

    reg_anal_b2 = ttk.Button(
        reg_anal_win_lf1, text='Classwise Analysis', command=reg_anal_b2_func)
    reg_anal_b2.grid(row=0, column=1, padx=10, pady=10)
    
    # Genderwise analysis button program
    
    def reg_anal_b3_func():
        
        speak('Performing genderwise analysis sir')

    reg_anal_b3 = ttk.Button(
        reg_anal_win_lf1, text='Genderwise Analysis', command=reg_anal_b3_func)
    reg_anal_b3.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    reg_anal_win.mainloop()
