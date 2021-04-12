from tkinter import *
from tkinter import ttk
import os
import pandas as pd


def reg_func(stu_name, stu_class, stu_school, stu_mail, stu_cont_no, remarks, fee_depo_pattern, stu_gender, tot_fee, admini_date):
    
    if os.path.isfile('Students_Records.xlsx')==False:

        table=pd.DataFrame({'Name':[stu_name], 'Class':[stu_class], 'School':[stu_school], 'EMail ID':[stu_mail], 'Contact Number':[stu_cont_no], 'Remarks':[remarks], 'Deposit Pattern':[fee_depo_pattern], 'Gender':[stu_gender], 'Total Fee':[tot_fee], 'Joining Date':[admini_date]}).set_index('Name')
        
        table.to_excel('Students_Records.xlsx')
        print('Students_Records.xlsx made sir and records of '+stu_name+' stored')
        
    else:
        
        table=pd.read_excel('Students_Records.xlsx').set_index('Name')
        
        table.loc[stu_name]=[stu_class, stu_school, stu_mail, stu_cont_no, remarks, fee_depo_pattern, stu_gender, tot_fee, admini_date]
        
        table.to_excel('Students_Records.xlsx')
        print('Student_Records.xlsx updated with the information about '+stu_name+' sir.')