# This file contains program to store records of all fee depositors

# Importing necessary libraries
from tkcalendar import Calendar,DateEntry
print('Importing necessary libraries for storing deposits...')
from Classes import *
from tkinter import ttk
from tkinter import *
from datetime import datetime

def record_deposits():

    # Preparing deposits record acceptor window

    print('Preparing deposits record acceptor window...')
    rec_depo = Tk()
    rec_depo_gui = window(rec_depo, 'Deposits')

    rec_depo_lf1 = LabelFrame(rec_depo, text='Form')
    rec_depo_lf1.grid(row=1, column=0, columnspan=3)

    # Preparing labels and combobox for name
    
    rec_depo_l1=Label(rec_depo_lf1)
    rec_depo_l1_gui=window.label(rec_depo_l1, 'Name of depositor: ', 0, 0)
    
    options=['Sam','Angel','Rahul']
    
    rec_depo_combobox1=ttk.Combobox(rec_depo_lf1)
    rec_depo_combobox1_gui=window.combobox(rec_depo_combobox1, options, 0, 1)
    
    # Preparing labels and entry for fees to be deposited

    rec_depo_l2=Label(rec_depo_lf1)
    rec_depo_l2_gui=window.label(rec_depo_l2, 'Fees to be deposited: ', 1, 0)
    
    rec_depo_e1=Entry(rec_depo_lf1)
    rec_depo_e1_gui=window.entry(rec_depo_e1, 1, 1)
    
    # Preparing labels and calendar for date of this fee submittion
    
    rec_depo_l3=Label(rec_depo_lf1)
    rec_depo_l3_gui=window.label(rec_depo_l3, 'Date of fee deposition: ', 2, 0)
    
    cal=DateEntry(rec_depo_lf1)
    cal_gui=window.dateentry(cal, 2,1)
    
    # Making submit button
    
    rec_depo_b1=ttk.Button(rec_depo, text='Submit', cursor='wait')
    rec_depo_b1.grid(row=2,column=1,padx=5, pady=5)
    
    rec_depo.mainloop()
