# Program to show calendar and more for calendar button

# Importing necessary libraries
from tkinter import *
from tkinter import ttk
import time
from Classes import *
from tkcalendar import Calendar
from datetime import datetime
import threading

def time_stamp():

    cal_win=Tk()
    cal_win_gui=window(cal_win, 'Calendar')
    
    f=Frame(cal_win)
    f.grid(row=1, column=1)
    
    f_cal1=Calendar(f)
    f_cal1.grid(row=1, column=0, padx=5, pady=5)
    
    def cal_win_b1_func():
        import webbrowser
        webbrowser.open('https://calendar.google.com/calendar/u/0/r?pli=1')
    
    cal_win_b1=ttk.Button(cal_win, text='Google Calendar', command=cal_win_b1_func)
    cal_win_b1.grid(row=2, column=1, padx=5, pady=5)
    
    def main_win_time():
        while True:
            time.sleep(1)
            f_l1=Label(f, text=datetime.now().strftime('%A %B %d %I:%M:%S %p'), font=('Helvetica', 15), fg='white', bg='blue')
            f_l1.grid(row=0, column=0, padx=5, pady=5)
    
    threading.Thread(target=main_win_time).start()
    
    cal_win.mainloop()
