# Python file containing program to access records of students who registered names.

# Importing necessary libraries...
from tkinter import ttk
from Classes import *
from tkinter import *
import pandas as pd
import threading
import time
from pandastable import Table

table = pd.read_excel('Students_Records.xlsx')
print('Table from records.py')

def access_records():

    # Preparing window for accessing records

    print('Preparing registration records window...')
    registration_records_window = Tk()
    registration_records_window_gui = window(
        registration_records_window, 'Registration Records')

    reg_rec_lf1 = LabelFrame(registration_records_window,
                             text='Records', relief='groove', bd=10)
    reg_rec_lf1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Asking for the kind of data user wants to access

    reg_rec_l1 = Label(reg_rec_lf1)
    reg_rec_gui = window.label(
        reg_rec_l1, 'Please select whose data you want to access: ', 0, 0)
    
    names=table['Name'].to_list()
    names.sort()
    classes = [str(i) for i in list(table.Class.unique())]

    options = ['All Classes']+classes+names  # Contains all names and classes

    variable=StringVar()

    reg_rec_combobox1 = ttk.Combobox(reg_rec_lf1, textvariable=variable)
    reg_rec_combobox1_gui = window.combobox(reg_rec_combobox1, options, 0, 1)
    
    f1=Frame(registration_records_window, relief='groove', bd=10)
    f1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    
    def reg_rec_b1_function():
        
        if reg_rec_combobox1.get() in names:
            
            tb=Table(f1, dataframe=table.loc[table['Name'] == reg_rec_combobox1.get()], showtoolbar=True, showstatusbar=True)
            tb.show()
            
        if reg_rec_combobox1.get()=='All Classes':
            
            tb=Table(f1, dataframe=table, showtoolbar=True, showstatusbar=True)
            tb.show()
            
        if reg_rec_combobox1.get() in classes:
            
            try:
                rec_class = int(reg_rec_combobox1.get())
            except Exception:
                rec_class = reg_rec_combobox1.get()
            
            tb = Table(f1, dataframe=table.loc[table['Class'] == rec_class], showtoolbar=True, showstatusbar=True)
            tb.show()
            
        

    reg_rec_b1 = ttk.Button(reg_rec_lf1, text='Submit', command=reg_rec_b1_function)
    reg_rec_b1.grid(row=0, column=2)
    
    reg_rec_b2=ttk.Button(registration_records_window, text='Exit', command=registration_records_window.destroy)
    reg_rec_b2.grid(row=3, column=1, padx=5, pady=5)

    registration_records_window.mainloop()
