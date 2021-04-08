# Python file containing program to analyse registration records

# Importing necessary libraries
from Classes import *
from tkinter import *
from tkinter import ttk


def registration_analysis():

    # Preparing window for analysis

    print('Preparing window for registration analysis...')
    reg_anal_win = Tk()
    reg_anal_win_gui = window(reg_anal_win, 'Registration Analysis')

    reg_anal_win_lf1 = LabelFrame(reg_anal_win, text='Analysis Section')
    reg_anal_win_lf1.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    # Asking for the type of analysis user wants

    reg_anal_b1 = ttk.Button(reg_anal_win_lf1, text='Monthly Analysis',cursor='wait')
    reg_anal_b1.grid(row=0, column=0, padx=10, pady=10)

    reg_anal_b2 = ttk.Button(
        reg_anal_win_lf1, text='Classwise Analysis', cursor='wait')
    reg_anal_b2.grid(row=0, column=1, padx=10, pady=10)
    
    reg_anal_b3=ttk.Button(reg_anal_win_lf1, text='Genderwise Analysis', cursor='wait')
    reg_anal_b3.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    reg_anal_win.mainloop()
