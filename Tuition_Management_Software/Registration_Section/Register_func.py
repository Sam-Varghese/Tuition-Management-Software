from tkinter import *
from tkinter import ttk
import pandas as pd
import threading

table = pd.read_excel('Students_Records.xlsx')
table.set_index('Name',inplace=True)
print('sheets table sir:')

def reg_func(stu_name, stu_class, stu_school, stu_mail, stu_cont_no, remarks, fee_depo_pattern, stu_gender, tot_fee, admini_date):
    
    print('Starting the data works of registration')

        
    table.loc[stu_name]=[stu_class, stu_school, stu_mail, stu_cont_no, remarks, fee_depo_pattern, stu_gender, tot_fee, admini_date]
    
    table.sort_values(by=['Name'], inplace=True)
    print('DataFrame sorted alphabatically sir')
    table.reset_index(inplace=True)
    table.to_excel('Students_Records.xlsx')
    print('Student_Records.xlsx updated with the information about '+stu_name+' sir.')
