# Python File containing program to register names, and made for the register button of main window.

# Importing necessary librariesthreading
print('Importing necessary libraries for register button...')
from Classes import *
from tkinter import ttk
from tkinter import *
import pandas as pd
import time
import string
import threading
from tkcalendar import DateEntry
import pandas as pd
try:
    table = pd.read_excel('Students_Records.xlsx')
except Exception:
    table=pd.DataFrame({'Name':[],'Class':[],'School':[],'EMail ID':[],'Contact Number':[],'Remarks':[],'Deposit Pattern':[],'Gender':[],'Total Fee':[],'Joining Date':[]})

def register_names():

    # Preparing registration window---

    print('Preparing register window...')
    register_names_window = Tk()
    register_names_window_gui = window(register_names_window, 'Registration')

    reg_lf1 = LabelFrame(register_names_window, text='Register', relief='groove', bd=10)
    reg_lf1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Preparing labels and entry boxes for name---

    reg_l1 = Label(reg_lf1)
    # Names should be unique , pls read readme of this folder to understand why I did so
    reg_l1_gui = window.label(reg_l1, 'Name of student: ', 0, 0)

    reg_e1 = Entry(reg_lf1)
    reg_e1_gui = window.entry(reg_e1, 0, 1)

    def distinct_name_checker():

        names=table['Name'].to_list()
        
        def start_nam_check():

            while True:

                if reg_e1.get() == '':
                    time.sleep(2)

                else:
                    if string.capwords(reg_e1.get()) in names:
                        print('Name repetetion detected')
                        reg_e1['bg'] = 'red'
                        time.sleep(1)

                    else:
                        reg_e1['bg'] = 'white'

        threading.Thread(target=start_nam_check).start()
        
    distinct_name_checker()

    # Preparing labels and entry boxes for class---

    reg_l2 = Label(reg_lf1)

    # Class can be any other than 10, 11, 12 like 10th applied , therefore no combobox has been used with specific options.

    reg_l2_gui = window.label(reg_l2, 'Class of student: ', 1, 0)

    reg_e2 = Entry(reg_lf1)
    reg_e2_gui = window.entry(reg_e2, 1, 1)

    # Preparing labels and entry boxes for school---

    reg_l3 = Label(reg_lf1)
    reg_l3_gui = window.label(reg_l3, 'School of student: ', 2, 0)

    reg_e3 = Entry(reg_lf1)
    reg_e3_gui = window.entry(reg_e3, 2, 1)

    # Preparing labels and entry boxes for email id---

    reg_l4 = Label(reg_lf1)
    reg_l4_gui = window.label(reg_l4, 'E-Mail ID of student: ', 3, 0)

    reg_e4 = Entry(reg_lf1)
    reg_e4.insert(0, '@gmail.com')
    reg_e4_gui = window.entry(reg_e4, 3, 1)

    # Preparing labels and entry boxes for contact number---

    reg_l5 = Label(reg_lf1)
    reg_l5_gui = window.label(
        reg_l5, 'Contact numbers( separated by commas ): ', 4, 0)

    reg_e5 = Entry(reg_lf1)
    reg_e5_gui = window.entry(reg_e5, 4, 1)

    def valid_con_checker():
        print('Starting valid con checker')
        while True:

            for i in reg_e5.get().split(','):
                if i.isdigit() == '':
                    reg_e5['bg'] = 'white'
                    time.sleep(2)

                if (i.isdigit() == False and i != '') or (i.isdigit() and len(i) != 10):
                    reg_e5['bg'] = 'red'
                    print('Invalid contact number detected')
                    time.sleep(1)
                if i.isdigit() and len(i) == 10:
                    reg_e5['bg'] = 'white'

    threading.Thread(target=valid_con_checker).start()

    # Preparing labels and entry boxes for remarks about student---

    reg_l6 = Label(reg_lf1)
    reg_l6_gui = window.label(reg_l6, 'Remarks about student: ', 5, 0)

    reg_e6 = Entry(reg_lf1)
    reg_e6.insert(0, 'None')
    reg_e6_gui = window.entry(reg_e6, 5, 1)

    # Preparing labels and comboboxes for remarks about pattern of fee deposits---

    reg_l7 = Label(reg_lf1)
    reg_l7_gui = window.label(reg_l7, 'Fee deposit pattern: ', 6, 0)

    options = ['Yearly', 'Monthly']
    reg_combobox1_variable = StringVar()

    reg_combobox1 = ttk.Combobox(reg_lf1, textvariable=reg_combobox1_variable)
    reg_combobox1_gui = window.combobox(reg_combobox1, options, 6, 1)

    # Preparing labels and comboboxes for gender details

    reg_l8 = Label(reg_lf1)
    reg_l8_gui = window.label(reg_l8, 'Gender of student: ', 7, 0)

    options = ['Male', 'Female']
    reg_combobox2_variable = StringVar()

    reg_combobox2 = ttk.Combobox(reg_lf1, textvariable=reg_combobox2_variable)
    reg_combobox2_gui = window.combobox(reg_combobox2, options, 7, 1)


    # Preparing labels and entry boxes for fees to be deposited

    reg_l9 = Label(reg_lf1)
    reg_l9_gui = window.label(reg_l9, 'Monthly/Yearly fee: ', 8, 0)

    reg_e7 = Entry(reg_lf1)
    reg_e7_gui = window.entry(reg_e7, 8, 1)

    def fee_checker():

        while True:

            if reg_e7.get().isdigit() == False and reg_e7.get() != '':
                reg_e7['bg'] = 'red'
                time.sleep(1)
            if reg_e7.get().isdigit():
                reg_e7['bg'] = 'white'

    threading.Thread(target=fee_checker).start()
    # Preparing labels and calendar for remarks about date of admission---

    reg_l10 = Label(reg_lf1)
    reg_l10_gui = window.label(reg_l10, 'Date of admission: ', 9, 0)

    cal = DateEntry(reg_lf1, background='blue', foreground='silver')
    cal_gui = window.dateentry(cal, 9, 1)

    # Making buttons for submitting data.

    def reg_b1_gui():
        from Registration_Section import Register_func
        Register_func.reg_func(string.capwords(reg_e1.get()), string.capwords(reg_e2.get()), string.capwords(reg_e3.get()), reg_e4.get(), reg_e5.get(), reg_e6.get().capitalize(), reg_combobox1.get(), reg_combobox2.get(), reg_e7.get(), cal.get())
        
        register_names_window.destroy()

    reg_b1 = ttk.Button(register_names_window,
                        text='Submit', command=reg_b1_gui)
    reg_b1.grid(row=2, column=1, padx=5, pady=5)

    register_names_window.mainloop()
