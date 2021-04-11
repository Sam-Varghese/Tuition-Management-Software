# Program to show calendar and more for calendar button

# Importing necessary libraries
from tkinter import *
from tkinter import ttk
from Classes import *
from tkcalendar import Calendar
from datetime import datetime

def time_stamp():

    cal_win=Tk()
    cal_win_gui=window(cal_win, 'Calendar')
    
    cal=Calendar(cal_win)
    cal.grid(row=1, column=1, padx=5, pady=5)
    
    def cal_win_b1_func():
        import webbrowser
        webbrowser.open('https://calendar.google.com/calendar/u/0/r?pli=1')
    
    cal_win_b1=ttk.Button(cal_win, text='Google Calendar', command=cal_win_b1_func)
    cal_win_b1.grid(row=2, column=1)
    
    cal_win.mainloop()
