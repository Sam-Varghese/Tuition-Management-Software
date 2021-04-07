# Python File containing program to register names, and made for the register button of main window.

# Importing necessary libraries
from tkinter import *
from tkinter import ttk
from Classes import *
print('Importing necessary libraries for register button...')


def register_names():

    # Preparing registration window---

    print('Preparing register window...')
    register_names_window = Tk()
    register_names_window_gui = window(register_names_window, 'Registeration')

    reg_lf1 = LabelFrame(register_names_window, text='Register')
    reg_lf1.grid(row=1, column=0, columnspan=3)

    # Preparing labels and entry boxes for name---

    reg_l1 = Label(reg_lf1)
    reg_l1_gui = window.label(reg_l1, 'Name of student: ', 0, 0)

    reg_e1 = Entry(reg_lf1)
    reg_e1_gui = window.entry(reg_e1, 0, 1)

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
    reg_e4_gui = window.entry(reg_e4, 3, 1)

    # Preparing labels and entry boxes for contact number---

    reg_l5 = Label(reg_lf1)
    reg_l5_gui = window.label(
        reg_l5, 'Contact numbers( separated by commas ): ', 4, 0)

    reg_e5 = Entry(reg_lf1)
    reg_e5_gui = window.entry(reg_e5, 4, 1)

    # Preparing labels and entry boxes for remarks about student---

    reg_l6 = Label(reg_lf1)
    reg_l6_gui = window.label(reg_l6, 'Remarks about student: ', 5, 0)

    reg_e6 = Entry(reg_lf1)
    reg_e6_gui = window.entry(reg_e6, 5, 1)

    # Preparing labels and entry boxes for remarks about date of admission---

    reg_l7 = Label(reg_lf1)
    reg_l7_gui = window.label(reg_l7, 'Date of admission: ', 6, 0)

    reg_e7 = Entry(reg_lf1)
    reg_e7.insert(0, present_time_stamp())
    reg_e7_gui = window.entry(reg_e7, 6, 1)

    # Making buttons for submitting data and entering more.

    reg_b1 = ttk.Button(register_names_window, text='Submit')
    reg_b1.grid(row=2, column=1, padx=10, pady=10)

    reg_b2 = ttk.Button(register_names_window, text='Continue')
    reg_b2.grid(row=3, column=1, padx=10, pady=10)

    register_names_window.mainloop()
