# This file contains program to store records of all fee depositors

# Importing necessary libraries
from tkinter import *
import threading
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tkcalendar import  DateEntry
import string
import pandas as pd
import time
import pyttsx3
import win32api

from tkinter import ttk

from Classes import *


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'GSpread-2ecbd68261be.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('Students_Records').sheet1

data = wks.get_all_values()
headers = data.pop(0)

table = pd.DataFrame(data, columns=headers)

wks = gc.open('Students_Records').worksheet('Sheet2')

data = wks.get_all_values()
headers = data.pop(0)

wks = gc.open('Students_Records').worksheet('Sheet2')

data = wks.get_all_values()
headers = data.pop(0)

sh = gc.open('Students_Records')

worksheet = sh.get_worksheet(1)

lock = threading.Lock()


def speak(text, lock=lock):
    
    def process(text, lock):
        lock.acquire()
        pyttsx3.speak(text)
        lock.release()
    threading.Thread(target=process, args=(text, lock)).start()


def record_deposits():
    rec_depo=Tk()
    rec_depo_gui=window(rec_depo, 'Fee Deposits')
    rec_depo_lf1=LabelFrame(rec_depo, text='Deposits', relief='groove', bd=10)
    rec_depo_lf1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Preparing labels and combobox for name

    options = table['Name'].to_list()

    rec_depo_l1 = Label(rec_depo_lf1)
    rec_depo_l1_gui = window.label(rec_depo_l1, 'Name of depositor: ', 0, 0)

    rec_depo_combobox1 = ttk.Combobox(rec_depo_lf1)
    rec_depo_combobox1_gui = window.combobox(rec_depo_combobox1, options, 0, 1)

    rec_depo_l1 = Label(rec_depo_lf1)
    rec_depo_l1_gui = window.label(rec_depo_l1, 'Name of depositor: ', 0, 0)



    variable = StringVar()

    rec_depo_combobox1 = ttk.Combobox(rec_depo_lf1, textvariable=variable)
    rec_depo_combobox1_gui = window.combobox(rec_depo_combobox1, options, 0, 1)

    # Preparing labels and entry for fees to be deposited

    rec_depo_l2 = Label(rec_depo_lf1)
    rec_depo_l2_gui = window.label(rec_depo_l2, 'Fees to be deposited: ', 1, 0)

    rec_depo_e1 = Entry(rec_depo_lf1)
    rec_depo_e1_gui = window.entry(rec_depo_e1, 1, 1)

    rec_depo_l2 = Label(rec_depo_lf1)
    rec_depo_l2_gui = window.label(rec_depo_l2, 'Fees to be deposited: ', 1, 0)

    rec_depo_e1 = Entry(rec_depo_lf1)
    rec_depo_e1_gui = window.entry(rec_depo_e1, 1, 1)

    def fee_depo_checker():

        while True:

            time.sleep(1)

            if rec_depo_e1.get() == '':

                rec_depo_e1['bg'] = 'white'

            if rec_depo_e1.get() != '' and rec_depo_e1.get().isdigit() == False:

                rec_depo_e1['bg'] = 'red'

            if rec_depo_e1.get().isdigit():

                rec_depo_e1['bg'] = 'white'

    threading.Thread(target=fee_depo_checker).start()

    # Preparing labels and for date of this fee submittion

    rec_depo_l3 = Label(rec_depo_lf1)
    rec_depo_l3_gui = window.label(
        rec_depo_l3, 'Date of fee deposition: ', 2, 0)

    cal = DateEntry(rec_depo_lf1, background='blue', foreground='silver')
    cal_gui = window.dateentry(cal, 2, 1)

    rec_depo_l3 = Label(rec_depo_lf1)
    rec_depo_l3_gui = window.label(
        rec_depo_l3, 'Date of fee deposition: ', 2, 0)

    cal = DateEntry(rec_depo_lf1, background='blue', foreground='silver')
    cal_gui = window.dateentry(cal, 2, 1)

    # Making submit button

    def rec_depo_b1_func():

        

        record = pd.DataFrame({'Name': [rec_depo_combobox1.get()], 'Class': [
            table[table['Name'] == rec_depo_combobox1.get()]['Class'].iloc[0]], 'Fee Deposited': [rec_depo_e1.get()], 'Deposition Date': [cal.get()], 'School': [table[table['Name'] == rec_depo_combobox1.get()]['School'].iloc[0]], 'EMail ID': [table[table['Name'] == rec_depo_combobox1.get()]['EMail ID'].iloc[0]], 'Contact Number': [table[table['Name'] == rec_depo_combobox1.get()]['Contact Number'].iloc[0]], 'Remarks': [table[table['Name'] == rec_depo_combobox1.get()]['Remarks'].iloc[0]], 'Deposit Pattern': [table[table['Name'] == rec_depo_combobox1.get()]['Deposit Pattern'].iloc[0]], 'Gender': [table[table['Name'] == rec_depo_combobox1.get()]['Gender'].iloc[0]], 'Total Fee': [table[table['Name'] == rec_depo_combobox1.get()]['Total Fee'].iloc[0]], 'Joining Date': [table[table['Name'] == rec_depo_combobox1.get()]['Joining Date'].iloc[0]]}).set_index('Name')
        new_table = pd.DataFrame(
            data, columns=headers)
        new_table.set_index('Name', inplace=True)

        new_table = new_table.append(record)

        new_table.sort_values(by=['Name'], inplace=True)
        print('Table sorted alphabatically sir')

        
        new_table.reset_index(inplace=True)
        worksheet.update([new_table.columns.values.tolist()]+new_table.values.tolist())
    
        new_table.to_excel('Deposit_Records.xlsx')
        print('All data saved successfully sir.')

        speak('Data of the depositor stored successfully sir')
        rec_depo.destroy()

    rec_depo_b1 = ttk.Button(rec_depo, text='Submit', command=rec_depo_b1_func)
    rec_depo_b1.grid(row=2, column=1, padx=5, pady=5)

    rec_depo_b1 = ttk.Button(rec_depo, text='Submit', command=rec_depo_b1_func)
    rec_depo_b1.grid(row=2, column=1, padx=5, pady=5)

    rec_depo.mainloop()
