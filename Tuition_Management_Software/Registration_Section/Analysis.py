# Python file containing program to analyse registration records

# Importing necessary libraries
from Classes import *
from tkinter import *
from tkinter import ttk
import threading


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

    reg_anal_b1 = ttk.Button(
        reg_anal_win_lf1, text='Monthly Analysis')
    reg_anal_b1.grid(row=0, column=0, padx=10, pady=10)

    reg_anal_b2 = ttk.Button(
        reg_anal_win_lf1, text='Classwise Analysis')
    reg_anal_b2.grid(row=0, column=1, padx=10, pady=10)

    reg_anal_b3 = ttk.Button(
        reg_anal_win_lf1, text='Genderwise Analysis')
    reg_anal_b3.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    reg_anal_win.mainloop()
