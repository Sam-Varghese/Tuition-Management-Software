# This folder contains program to access the records of fee depositors

# Importing necessary libraries
print('Importing necessary libraries for deposit records...')
import time
import threading
from Classes import *
from tkinter import ttk
from tkinter import *
import pandas as pd
from pandastable import Table
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'GSpread-2ecbd68261be.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('Students_Records').worksheet('Sheet2')

data = wks.get_all_values()
headers = data.pop(0)
table = pd.DataFrame(data, columns=headers)

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


def deposit_records():

    # Preparing window...
    print('Preparing deposit records accessor window...')
    depo_rec = Tk()
    depo_rec_gui = window(depo_rec, 'Deposit Records')

    depo_rec_lf1 = LabelFrame(depo_rec, text='Records', relief='groove', bd=10)
    depo_rec_lf1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Making labels and boxes for type of record user wants to access

    depo_rec_l1 = Label(depo_rec_lf1)
    depo_rec_l1_gui = window.label(
        depo_rec_l1, 'Please select whose records you want to access: ', 0, 0)

    classes=[str(i) for i in list(table.Class.unique())]
    names=list(table.Name.unique())
    names.sort()
    options = ['All History']+classes+names # Contains list of all names and classes

    variable=StringVar()
    depo_rec_combobox1 = ttk.Combobox(depo_rec_lf1, textvariable=variable)
    depo_rec_combobox1_gui = window.combobox(depo_rec_combobox1, options, 0, 1)
    
    # Program for submit button
    
    def depo_rec_b1_func():
        
        f1 = Frame(depo_rec, relief='groove', bd=10)
        f1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
        if depo_rec_combobox1.get() in classes:
            real_class = depo_rec_combobox1.get()
                
            tb=Table(f1, dataframe=table[table['Class']==real_class], showtoolbar=True, showstatusbar=True)
            tb.show()
            
        elif depo_rec_combobox1.get() in names:

            tb = Table(f1, dataframe=table.loc[table['Name'] == depo_rec_combobox1.get(
            )], showtoolbar=True, showstatusbar=True)
            tb.show()

        else:

            tb = Table(f1, dataframe=table,
                       showtoolbar=True, showstatusbar=True)
            tb.show()
        
        

    depo_rec_b1 = ttk.Button(depo_rec, text='Submit', command=depo_rec_b1_func)
    depo_rec_b1.grid(row=1, column=2, padx=5, pady=5)

    depo_rec.mainloop()
