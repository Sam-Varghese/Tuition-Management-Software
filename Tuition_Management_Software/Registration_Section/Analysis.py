# Python file containing program to analyse registration records

# Importing necessary libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from Classes import *
from tkinter import *
from tkinter import ttk
import threading
import matplotlib.pyplot as plt
import time
import pandas as pd

lock = threading.Lock()

print('Importing necessary libraries for records button...')
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'GSpread-2ecbd68261be.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('Students_Records').sheet1

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


def registration_analysis():

    # Preparing window for analysis

    print('Preparing window for registration analysis...')
    reg_anal_win = Tk()
    reg_anal_win_gui = window(reg_anal_win, 'Registration Analysis')

    reg_anal_win_lf1 = LabelFrame(
        reg_anal_win, text='Analysis Section', relief='groove', bd=10)
    reg_anal_win_lf1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Asking for the type of analysis user wants
    
    # Monthly analysis button program
    
    def reg_anal_b1_func():
        
        table['Joining Date']=pd.to_datetime(table['Joining Date'])
        final_table=table.groupby(table['Joining Date'].dt.strftime('%B %Y'))
        dic={}
        for i in final_table:
            
            dic[i[0]]=len(i[1].index)
            
        plt.barh(list(dic.keys()),list(dic.values()))
        plt.ylabel('Months')
        plt.xlabel('Students Count')
        plt.title('Monthly Analysis')
        plt.gcf().canvas.set_window_title('Monthly Analysis')
        plt.show()
        

    reg_anal_b1 = ttk.Button(
        reg_anal_win_lf1, text='Monthly Analysis', command=reg_anal_b1_func)
    reg_anal_b1.grid(row=0, column=0, padx=10, pady=10)
    
    # Classwise analysis button program
    
    def reg_anal_b2_func():
        
        unique_class=table.Class.unique()
        stu_count=[]
        for i in unique_class:
            stu_count.append(len(table[table['Class']==i].index))
        plt.barh(unique_class, stu_count)
        plt.ylabel('Classes')
        plt.xlabel('Strength')
        plt.title('Classwise Analysis')
        plt.gcf().canvas.set_window_title('Class Analysis')
        plt.show()
        print(list(unique_class), stu_count)
        

    reg_anal_b2 = ttk.Button(
        reg_anal_win_lf1, text='Classwise Analysis', command=reg_anal_b2_func)
    reg_anal_b2.grid(row=0, column=1, padx=10, pady=10)
    
    # Genderwise analysis button program
    
    def reg_anal_b3_func():
        
        graph=plt.bar(['Males', 'Females'], [len(table[table['Gender'] == 'Male'].index), len(
            table[table['Gender'] == 'Female'].index)])
        plt.title('Gender Analysis')
        plt.xlabel('Gender')
        plt.ylabel('Students Count')
        plt.gcf().canvas.set_window_title('Gender Analysis')
        graph[0].set_color('red')
        graph[1].set_color('pink')
        plt.show()
        

    reg_anal_b3 = ttk.Button(
        reg_anal_win_lf1, text='Genderwise Analysis', command=reg_anal_b3_func)
    reg_anal_b3.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    reg_anal_win.mainloop()
