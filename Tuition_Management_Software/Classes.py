# Creating classes for most occuring widgets of window

#Importing necessary libraries
from tkinter import *

def present_time_stamp():
    
    import datetime
    print('Entring time: ', datetime.datetime.now())
    return datetime.datetime.now()

class window():

    def __init__(self, window_name, title):

        window_name['background'] = 'blue'
        window_title = Label(window_name, text=title,
                             fg='white', bg='blue', font=('georgia', 25))
        window_title.grid(row=0, column=1)
        window_name.resizable(False, False) # Restricting resizing of window to prevent change in format of contents.

    def label(label_name, label_text, row_no, column_no):

        label_name['text'] = label_text
        label_name['bg'] = 'blue'
        label_name['fg'] = 'white'
        label_name['font'] = ('georgia', 15)
        label_name.grid(row=row_no, column=column_no, padx=10, pady=10,sticky='W')

    def entry(entry_name, row_no, column_no):

        entry_name['bg'] = 'snow'
        entry_name['fg'] = 'black'
        entry_name['font'] = ('helvetica', 15)
        entry_name.grid(row=row_no, column=column_no, padx=10, pady=10)

    def combobox(box_name, options, row_no, column_no):

        box_name['values'] = options
        box_name['state'] = 'readonly'
        box_name['font'] = ('georgia', 15)
        box_name.grid(row=row_no, column=column_no, padx=10, pady=10)
