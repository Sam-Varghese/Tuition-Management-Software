# This folder contains program to access the records of fee depositors

# Importing necessary libraries
print('Importing necessary libraries for deposit records...')
from tkinter import *
from tkinter import ttk
from Classes import *

def deposit_records():
    
    # Preparing window...
    print('Preparing deposit records accessor window...')
    depo_rec=Tk()
    depo_rec_gui=window(depo_rec, 'Deposit Records')
    
    depo_rec_lf1=LabelFrame(depo_rec, text='Records')
    depo_rec_lf1.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
    
    # Making labels and boxes for type of record user wants to access
    
    depo_rec_l1=Label(depo_rec_lf1)
    depo_rec_l1_gui=window.label(depo_rec_l1, 'Please select whose records you want to access: ', 0, 0)
    
    options=['Class 12th','Class 11th','Sam','Angel','Rahul']
    
    depo_rec_combobox1=ttk.Combobox(depo_rec_lf1)
    depo_rec_combobox1_gui=window.combobox(depo_rec_combobox1, options, 0, 1)
    
    depo_rec_b1 = ttk.Button(depo_rec, text='Submit', cursor='wait')
    depo_rec_b1.grid(row=1, column=3, padx=5, pady=5)
    
    depo_rec.mainloop()
