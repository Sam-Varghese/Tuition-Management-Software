# Python file containing program to access records of students who registered names.

# Importing necessary libraries...
from tkinter import ttk
from tkinter import *
from Classes import *
print('Importing necessary libraries for records button...')


def access_records():

    # Preparing window for accessing records

    print('Preparing registration records window...')
    registration_records_window = Tk()
    registration_records_window_gui = window(
        registration_records_window, 'Registration Records')

    reg_rec_lf1 = LabelFrame(registration_records_window, text='Records')
    reg_rec_lf1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Asking for the kind of data user wants to access

    reg_rec_l1 = Label(reg_rec_lf1)
    reg_rec_gui = window.label(
        reg_rec_l1, 'Please select whose data you want to access: ', 0, 0)

    options = ['All Classes', 'Class 9th', 'Class 10th',
               'Sam', 'Angel']  # Contains all names and classes

    reg_rec_combobox1 = ttk.Combobox(reg_rec_lf1)
    reg_rec_combobox1_gui = window.combobox(reg_rec_combobox1, options, 0, 1)

    reg_rec_b1 = ttk.Button(reg_rec_lf1, text='Submit', cursor='wait')
    reg_rec_b1.grid(row=0, column=2)

    registration_records_window.mainloop()
