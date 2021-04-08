# This file would contain program for the main window of this tuition management software.

# Importing necessary libraries.
# Classes is a file with a separate class for all important widgets
from Classes import window
from tkinter import ttk
from tkinter import *
print('Importing necessary libraries for main window...')

# Preparing the main window

print('Preparing main window...')
main_window = Tk()
main_window_gui = window(main_window, 'Paul Classes')

# Making label frames for putting buttons

# LabelFrame lf1 for registration

lf1 = LabelFrame(main_window, text='Registration Section')
lf1.grid(row=1, column=0, padx=10, pady=10)


def lf1_b1_function():

    print('Running register button program...')
    from Registration_Section import Register
    Register.register_names()


lf1_b1 = ttk.Button(lf1, text='Register', command=lf1_b1_function)
lf1_b1.pack(padx=5, pady=5)


def lf1_b2_function():

    print('Running registration records button program...')
    from Registration_Section import Records
    Records.access_records()


lf1_b2 = ttk.Button(lf1, text='Records', command=lf1_b2_function)
lf1_b2.pack(padx=5, pady=5)


def lf1_b3_function():

    print('Running registration analysis button program...')
    from Registration_Section import Analysis
    Analysis.registration_analysis()


lf1_b3 = ttk.Button(lf1, text='Analysis', command=lf1_b3_function)
lf1_b3.pack(padx=5, pady=5)

# LabelFrame lf2 for attendance

lf2 = LabelFrame(main_window, text='Attendance Section')
lf2.grid(row=1, column=1, padx=10, pady=10)

lf2_b1 = ttk.Button(lf2, text='Attendance')
lf2_b1.pack(padx=5, pady=5)

lf2_b2 = ttk.Button(lf2, text='Records')
lf2_b2.pack(padx=5, pady=5)

lf2_b3 = ttk.Button(lf2, text='Analysis')
lf2_b3.pack(padx=5, pady=5)

# LabelFrame lf3 for finance

lf3 = LabelFrame(main_window, text='Finance Section')
lf3.grid(row=1, column=2, padx=10, pady=10)

def lf3_b1_function():
    
    print('Running fee deposit button...')
    from Finance_Section import Deposits
    Deposits.record_deposits()

lf3_b1 = ttk.Button(lf3, text='Deposits', command=lf3_b1_function)
lf3_b1.pack(padx=5, pady=5)

lf3_b2 = ttk.Button(lf3, text='Records')
lf3_b2.pack(padx=5, pady=5)

lf3_b3 = ttk.Button(lf3, text='Defaulters')
lf3_b3.pack(padx=5, pady=5)

# LabelFrame lf4 for other useful programs

lf4 = LabelFrame(main_window, text='Extras')
lf4.grid(row=2, column=1, padx=10, pady=10)

lf4_b1 = ttk.Button(lf4, text='Google')
lf4_b1.pack(padx=5, pady=5)

lf4_b2 = ttk.Button(lf4, text='Youtube')
lf4_b2.pack(padx=5, pady=5)

lf4_b3 = ttk.Button(lf4, text='GeoGebra')
lf4_b3.pack(padx=5, pady=5)

# Putting window in mainloop

main_window.mainloop()
