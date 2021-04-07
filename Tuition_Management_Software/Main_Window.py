# This file would contain program for the main window of this tuition management software.

# Importing necessary libraries.

from tkinter import *
from tkinter import ttk
import pandas as pd

# Creating classes for most occuring widgets of window


class window():

    def __init__(self, window_name, title):

        window_name['background'] = 'blue'
        window_title = Label(window_name, text=title,
                             fg='white', bg='blue', font=('georgia', 20))
        window_title.grid(row=0, column=1)

    def label(self, label_name, label_text, row_no, column_no):

        label_name['text'] = label_text
        label_name['bg'] = 'blue'
        label_name['fg'] = 'white'
        label_name['font'] = ('georgia', 15)
        label_name.grid(row=row_no, column=column_no, padx=10, pady=10)

    def entry(self, entry_name, entry_text, row_no, column_no):

        entry_name['bg'] = 'snow'
        entry_name['fg'] = 'gold'
        entry_name['font'] = ('georgia', 15)
        entry_name.grid(row=row_no, column=column_no, padx=10, pady=10)

    def combobox(self, box_name, options, row_no, column_no):

        box_name['values'] = options
        box_name['state'] = 'readonly'
        box_name['font'] = ('georgia', 15)
        box_name.grid(row=row_no, column=column_no, padx=10, pady=10)

# Preparing the main window


main_window = Tk()
main_window_gui = window(main_window, 'Paul Classes')

# Making label frames for putting buttons

# LabelFrame lf1

lf1 = LabelFrame(main_window, text='Registration Section')
lf1.grid(row=1, column=0, padx=10, pady=10)

lf1_b1 = ttk.Button(lf1, text='Register')
lf1_b1.pack(padx=5,pady=5)

lf1_b2 = ttk.Button(lf1, text='Records')
lf1_b2.pack(padx=5,pady=5)

lf1_b3 = ttk.Button(lf1, text='Analysis')
lf1_b3.pack(padx=5,pady=5)

# LabelFrame lf2

lf2 = LabelFrame(main_window, text='Attendance Section')
lf2.grid(row=1, column=1, padx=10, pady=10)

lf2_b1 = ttk.Button(lf2, text='Attendance')
lf2_b1.pack(padx=5,pady=5)

lf2_b2 = ttk.Button(lf2, text='Records')
lf2_b2.pack(padx=5,pady=5)

lf2_b3 = ttk.Button(lf2, text='Analysis')
lf2_b3.pack(padx=5,pady=5)

# LabelFrame lf3

lf3 = LabelFrame(main_window, text='Finance Section')
lf3.grid(row=1, column=2, padx=10, pady=10)

lf3_b1 = ttk.Button(lf3, text='Deposits')
lf3_b1.pack(padx=5,pady=5)

lf3_b2 = ttk.Button(lf3, text='Records')
lf3_b2.pack(padx=5,pady=5)

lf3_b3 = ttk.Button(lf3, text='Defaulters')
lf3_b3.pack(padx=5,pady=5)

# LabelFrame lf4

lf4 = LabelFrame(main_window, text='Extras')
lf4.grid(row=2, column=1, padx=10, pady=10)

lf4_b1 = ttk.Button(lf4, text='Google')
lf4_b1.pack(padx=5,pady=5)

lf4_b2 = ttk.Button(lf4, text='Youtube')
lf4_b2.pack(padx=5,pady=5)

lf4_b3 = ttk.Button(lf4, text='GeoGebra')
lf4_b3.pack(padx=5,pady=5)

main_window.mainloop()
