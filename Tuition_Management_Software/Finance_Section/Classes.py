# Creating classes for most occuring widgets of window

# Importing necessary libraries
from datetime import date
from tkinter import *
from tkinter import ttk
import time
import string
import threading

def present_time_stamp():

    import datetime
    print('Entering time: ', datetime.datetime.now())
    return datetime.datetime.now()


class window():

    def __init__(self, window_name, title):

        #window_name['background'] = 'blue'
        window_name.geometry('+400+0')
        window_name.title(title)
        f=Frame(window_name, bg='gold', relief='groove', bd=5)
        f.grid(row=0, column=0, sticky='ew', columnspan=3, pady=5)
        window_title = Label(f, text=title,
                             fg='blue', font=('georgia', 25), bg='yellow')
        window_title.pack()
        # Restricting resizing of window to prevent change in format of contents.
        window_name.resizable(False, False)

    def label(label_name, label_text, row_no, column_no):

        label_name['text'] = label_text
        #label_name['bg'] = 'blue'
        #label_name['fg'] = 'white'
        label_name['font'] = ('georgia', 15)
        label_name.grid(row=row_no, column=column_no,
                        padx=5, pady=5, sticky='W')

    def entry(entry_name, row_no, column_no):

        #entry_name['bg'] = 'snow'
        entry_name['bd']=2
        #entry_name['fg'] = 'black'
        entry_name['font'] = ('helvetica', 15)
        entry_name.grid(row=row_no, column=column_no,
                        padx=5, pady=5, sticky='E')

    def dynamic_searchbox():
            while True:
                print('Dynamic checking')
                time.sleep(1)
                box_text = box_name.get()
                new_options = []
                for i in options:
                    i = i.lower()
                    box_text = box_text.lower()
                    if i.startswith(box_text):
                        new_options.append(string.capwords(i))
                new_options.sort()
                if new_options == []:
                    new_options = ['No similar name']
                box_name['values'] = new_options
        threading.Thread(target=dynamic_searchbox).start()
                
    def dateentry(dateentry_name, row_no, column_no):

        from datetime import datetime
        from tkcalendar import Calendar, DateEntry
        dateentry_name['font'] = ('helvetica', 13)
        dateentry_name['state']='readonly'
        dateentry_name['width']=20
        dateentry_name.grid(row=row_no, column=column_no, padx=5, pady=5, sticky='E')
