# This file would contain program for the main window of this tuition management software.

# Importing necessary libraries.

import time
import threading
import datetime
import webbrowser
def password_entry():
    
    from Security_Section import Password_Entry
    Password_Entry.password()

password_entry()  # This program wont go furthermore until the recursion happening in Password_Entry.py doesnt stops and exit button has also been disabled


print('\nActivating program...\n')


from Classes import window

from tkinter import ttk
from tkinter import *



# Preparing the main window



print('Preparing main window...')
main_window = Tk()
main_window_gui = window(main_window, 'Paul Classes')


f5 = Frame(main_window, bd=10, relief='groove')
f5.grid(row=1, column=1, padx=10, pady=10)

def main_win_time():
    while True:
        time.sleep(1)
        f5_l1=Label(f5, text=datetime.datetime.now().strftime('%B %d %A %I:%M:%S %p'), font=('Helvetica', 15), fg='blue')
        f5_l1.grid(row=0, column=0, padx=5, pady=5, columnspan=3)
    
threading.Thread(target=main_win_time).start()

def f5_b1_func():
    
    from Prog_Calendar import time_stamp
    time_stamp()

f5_b1=ttk.Button(f5, text='Calendar', command=f5_b1_func)
f5_b1.grid(row=1, column=1, padx=5, pady=5)


# Making label frames for putting buttons

# LabelFrame lf1 for registration section

lf1 = LabelFrame(main_window, text='Registration Department', relief='groove', bd=10)
lf1.grid(row=2, column=0, padx=10, pady=10)

# Program for registration button


def lf1_b1_function():
    
    print('Running register button program...')
    from Registration_Section import Register
    Register.register_names()


lf1_b1 = ttk.Button(lf1, text='Register',
                    command=lf1_b1_function)
lf1_b1.pack(padx=5, pady=5)

# Program for registration records button


def lf1_b2_function():
    
    print('Running registration records button program...')
    from Registration_Section import Records
    Records.access_records()


lf1_b2 = ttk.Button(lf1, text='Records',
                    command=lf1_b2_function)
lf1_b2.pack(padx=5, pady=5)

# Program for registration analysis button


def lf1_b3_function():
    
    print('Running registration analysis button program...')
    from Registration_Section import Analysis
    Analysis.registration_analysis()


lf1_b3 = ttk.Button(lf1, text='Analysis',
                    command=lf1_b3_function)
lf1_b3.pack(padx=5, pady=5)

# LabelFrame lf2 for attendance section

lf2 = LabelFrame(main_window, text='Attendance Department', relief='groove', bd=10)
lf2.grid(row=2, column=1, padx=10, pady=10)

# Program for attendance button

lf2_b1 = ttk.Button(lf2, text='Attendance')
lf2_b1.pack(padx=5, pady=5)

# Program for attendance records button

lf2_b2 = ttk.Button(lf2, text='Records')
lf2_b2.pack(padx=5, pady=5)

# Program for attendance analysis button

lf2_b3 = ttk.Button(lf2, text='Analysis')
lf2_b3.pack(padx=5, pady=5)

# LabelFrame lf3 for finance section

lf3 = LabelFrame(main_window, text='Finance Department', relief='groove', bd=10)
lf3.grid(row=2, column=2, padx=10, pady=10)

# Program for deposit section


def lf3_b1_function():
    
    print('Running fee deposit button...')
    from Finance_Section import Deposits
    Deposits.record_deposits()


lf3_b1 = ttk.Button(lf3, text='Deposits',
                    command=lf3_b1_function)
lf3_b1.pack(padx=5, pady=5)

# Program for fee deposit records button


def lf3_b2_function():
    
    print('Running fee deposit records...')
    from Finance_Section import Records
    Records.deposit_records()


lf3_b2 = ttk.Button(lf3, text='Records',
                    command=lf3_b2_function)
lf3_b2.pack(padx=5, pady=5)

# Program for fee defaulters button

def lf3_b3_func():
    from Finance_Section import Defaulters
    Defaulters.defaulter()
lf3_b3 = ttk.Button(lf3, text='Defaulters', command=lf3_b3_func)
lf3_b3.pack(padx=5, pady=5)

# LabelFrame lf4 for other extra softwares

lf4 = LabelFrame(main_window, text='Important Softwares', relief='groove', bd=10)
lf4.grid(row=3, column=1, padx=10, pady=10)

# Program for Google


def lf4_b1_function():
    
    print('Running google apps button...')
    from Extra_Softwares import Google
    Google.google_window()


lf4_b1 = ttk.Button(lf4, text='Google', command=lf4_b1_function)
lf4_b1.pack(padx=5, pady=5)

# Program for YouTube button


def lf4_b2_function():
    
    webbrowser.open('https://www.youtube.com/')
    
    print('Running YouTube apps button sir')

lf4_b2 = ttk.Button(lf4, text='Youtube', command=lf4_b2_function)
lf4_b2.pack(padx=5, pady=5)

# Program for GeoGebra button


def lf4_b3_function():
    
    print('Running GeoGebra apps button...')
    from Extra_Softwares import GeoGebra
    GeoGebra.geogebra()


lf4_b3 = ttk.Button(lf4, text='GeoGebra',
                    command=lf4_b3_function)  # Mainly used for scientific maths , my father uses it , so I included also
lf4_b3.pack(padx=5, pady=5)

# Program for spotify button


def lf4_b4_function():

    webbrowser.open('https://open.spotify.com/')
    
    print('Running spotify button program...')


# Teachers should also listen to spotify :)
lf4_b4 = ttk.Button(lf4, text='Spotify', command=lf4_b4_function)
lf4_b4.pack(padx=5, pady=5)

# Program for exit button


def main_win_b1_func():

    
    main_window.destroy()
    print('\nTerminating the program...\n')


main_win_b1 = ttk.Button(main_window, text='Exit', command=main_win_b1_func)
main_win_b1.grid(row=4, column=1, padx=5, pady=5)

# Program for shut down button


def main_win_b2_func():

    
    pywhatkit.shutdown(time=5)
    print('\nShutting pc down...\n')


main_win_b2 = ttk.Button(main_window, text='Shut Down',
                         command=main_win_b2_func)
main_win_b2.grid(row=5, column=1, padx=5, pady=5)


# Putting window in mainloop

main_window.mainloop()
