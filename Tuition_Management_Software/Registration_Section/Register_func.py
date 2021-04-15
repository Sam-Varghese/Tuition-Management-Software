from tkinter import *
from tkinter import ttk
import pandas as pd
import threading
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'GSpread-2ecbd68261be.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('Students_Records').sheet1

data = wks.get_all_values()
headers = data.pop(0)

table = pd.DataFrame(data, columns=headers)
table.set_index('Name',inplace=True)
print('sheets table sir:')

sh = gc.open('Students_Records')
worksheet = sh.sheet1

def reg_func(stu_name, stu_class, stu_school, stu_mail, stu_cont_no, remarks, fee_depo_pattern, stu_gender, tot_fee, admini_date):
    
    print('Starting the data works of registration')

        
    table.loc[stu_name]=[stu_class, stu_school, stu_mail, stu_cont_no, remarks, fee_depo_pattern, stu_gender, tot_fee, admini_date]
    
    table.sort_values(by=['Name'], inplace=True)
    print('DataFrame sorted alphabatically sir')
    
    def fun():
        table.reset_index(inplace=True)
        worksheet.update([table.columns.values.tolist()]+table.values.tolist())
        print('Threading work done')
    threading.Thread(target=fun).start()
    print('Student_Records.xlsx updated with the information about '+stu_name+' sir.')
