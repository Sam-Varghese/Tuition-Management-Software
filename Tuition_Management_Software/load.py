import time
start=time.time()
from tkinter import *
from tkinter import ttk
from Classes import *
win=Tk()
win_gui=window(win, 'Syncing')

def syncing():
    global end
    import pandas as pd
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import pandas as pd
    prog_bar['value']=10
    win.update_idletasks()
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'GSpread-2ecbd68261be.json', scope)
    gc = gspread.authorize(credentials)
    prog_bar['value']=15
    win.update_idletasks()
    wks = gc.open('Students_Records').sheet1
    data = wks.get_all_values()
    headers = data.pop(0)
    reg_sheets_table = pd.DataFrame(data, columns=headers)
    prog_bar['value']=20
    win.update_idletasks()
    print('\nPrinting registration table (without setting index) from google sheets: \n')
    print(reg_sheets_table.head())
    print('\nPrinting registration table with names column as its index: \n')
    reg_sheets_table['Name'] = reg_sheets_table['Name'].str.title()
    reg_sheets_table['School']=reg_sheets_table['School'].str.title()
    reg_sheets_table['Remarks']=reg_sheets_table['Remarks'].str.capitalize()
    reg_sheets_table['Deposit Pattern'] = reg_sheets_table['Deposit Pattern'].str.title()
    reg_sheets_table['Gender']=reg_sheets_table['Gender'].str.title()
    reg_sheets_table['Joining Date'] = pd.to_datetime(reg_sheets_table['Joining Date'])
    reg_sheets_table['Joining Date'] = reg_sheets_table['Joining Date'].dt.strftime('%d/%m/%Y')
    reg_sheets_table['Class'] = reg_sheets_table['Class'].astype('str')
    reg_sheets_table['Class'] = reg_sheets_table['Class'].str.title()
    reg_sheets_table.set_index('Name', inplace=True)
    print(reg_sheets_table.head())
    prog_bar['value']=25
    win.update_idletasks()
    
    reg_excel_table=pd.read_excel('Students_Records.xlsx')
    print('\nPrinting registration excel data (Without setting index):\n')
    print(reg_excel_table.head())
    reg_excel_table['Name'] = reg_excel_table['Name'].str.title()
    reg_excel_table['School']=reg_excel_table['School'].str.title()
    reg_excel_table['Remarks']=reg_excel_table['Remarks'].str.capitalize()
    reg_excel_table['Deposit Pattern'] = reg_excel_table['Deposit Pattern'].str.title()
    reg_excel_table['Gender']=reg_excel_table['Gender'].str.title()
    reg_excel_table['Joining Date'] = pd.to_datetime(reg_excel_table['Joining Date'])
    reg_excel_table['Joining Date'] = reg_excel_table['Joining Date'].dt.strftime('%d/%m/%Y')
    reg_excel_table['Class'] = reg_excel_table['Class'].astype('str')
    reg_excel_table['Class'] = reg_excel_table['Class'].str.title()
    reg_excel_table.set_index('Name',inplace=True)
    print('\nPrinting registration excel data after setting index:\n')
    print(reg_excel_table.head())
    prog_bar['value']=30
    win.update_idletasks()
    
    wks = gc.open('Students_Records').worksheet('Sheet2')
    data = wks.get_all_values()
    headers = data.pop(0)
    depo_sheets_table = pd.DataFrame(data, columns=headers)
    depo_sheets_table['Name'] = depo_sheets_table['Name'].str.title()
    depo_sheets_table['Class']=depo_sheets_table['Class'].astype('str')
    depo_sheets_table['Class']=depo_sheets_table['Class'].str.title()
    depo_sheets_table['Deposition Date']=pd.to_datetime(depo_sheets_table['Deposition Date'])
    depo_sheets_table['Deposition Date']=depo_sheets_table['Deposition Date'].dt.strftime('%d/%m/%Y')
    depo_sheets_table['School']=depo_sheets_table['School'].str.title()
    depo_sheets_table['Remarks']=depo_sheets_table['Remarks'].str.capitalize()
    depo_sheets_table['Deposit Pattern']=depo_sheets_table['Deposit Pattern'].str.title()
    depo_sheets_table['Gender']=depo_sheets_table['Gender'].str.title()
    depo_sheets_table['Joining Date']=pd.to_datetime(depo_sheets_table['Joining Date'])
    depo_sheets_table['Joining Date'] = depo_sheets_table['Joining Date'].dt.strftime(
        '%d/%m/%Y')
    prog_bar['value']=35
    win.update_idletasks()
    print('\nPrinting sheets deposition table without setting index:\n')
    print(depo_sheets_table.head())
    depo_sheets_table.set_index('Name', inplace=True)
    print('\nPrinting sheets deposition table after setting index:\n')
    print(depo_sheets_table.head())
    prog_bar['value']=40
    win.update_idletasks()
    
    depo_excel_table = pd.read_excel('Deposit_Records.xlsx')
    depo_excel_table = pd.DataFrame(data, columns=headers)
    depo_excel_table['Name'] = depo_excel_table['Name'].str.title()
    depo_excel_table['Class'] = depo_excel_table['Class'].astype('str')
    depo_excel_table['Class'] = depo_excel_table['Class'].str.title()
    depo_excel_table['Deposition Date'] = pd.to_datetime(
        depo_excel_table['Deposition Date'])
    depo_excel_table['Deposition Date'] = depo_excel_table['Deposition Date'].dt.strftime(
        '%d/%m/%Y')
    depo_excel_table['School'] = depo_excel_table['School'].str.title()
    depo_excel_table['Remarks'] = depo_excel_table['Remarks'].str.capitalize()
    depo_excel_table['Deposit Pattern'] = depo_excel_table['Deposit Pattern'].str.title()
    depo_excel_table['Gender'] = depo_excel_table['Gender'].str.title()
    depo_excel_table['Joining Date'] = pd.to_datetime(
        depo_excel_table['Joining Date'])
    depo_excel_table['Joining Date'] = depo_excel_table['Joining Date'].dt.strftime('%d/%m/%Y')
    print('\nDeposit records from excel without setting index:\n')
    print(depo_excel_table.head())
    print('\nDeposit records from excel after setting index:\n')
    depo_excel_table.set_index('Name' , inplace=True)
    print(depo_excel_table.head())
    prog_bar['value']=45
    win.update_idletasks()
    
    final_reg_table=reg_sheets_table.combine_first(reg_excel_table)
    final_reg_table.sort_index(inplace=True)
    print('\nPrinting final registration table\n')
    print(final_reg_table.head())
    prog_bar['value']=50
    win.update_idletasks()
    
    final_depo_table=depo_sheets_table.combine_first(depo_excel_table)
    final_depo_table.sort_index(inplace=True)
    print('\nPrinting final deposition table\n')
    print(final_depo_table.head())
    prog_bar['value']=60
    win.update_idletasks()
    
    final_reg_table.to_excel('Students_Records.xlsx')
    print('\nFinal registration records added in excel')
    final_depo_table.to_excel('Deposit_Records.xlsx')
    prog_bar['value']=70
    win.update_idletasks()
    final_depo_table.reset_index(inplace=True)
    final_reg_table.reset_index(inplace=True)
    print('Final deposit records added in excel')
    sh = gc.open('Students_Records')
    worksheet = sh.sheet1
    worksheet.update([final_reg_table.columns.values.tolist()
                      ]+final_reg_table.values.tolist())
    prog_bar['value']=80
    win.update_idletasks()
    print('Final registration record added to google sheets')
    worksheet = sh.get_worksheet(1)
    worksheet.update([final_depo_table.columns.values.tolist()] +
                     final_depo_table.values.tolist())
    print('Final deposition table added to google sheets.')
    prog_bar['value']=100
    win.update_idletasks()
    time.sleep(1)
    win.destroy()
    end = time.time()
    print('\nTotal time taken for syncing: ', end-start, ' seconds.')


prog_bar = ttk.Progressbar(win, orient=HORIZONTAL,
                           length=400, mode='determinate')
prog_bar.grid(row=1, column=1, padx=10, pady=10)

win_b1=ttk.Button(win, text='Start', command=syncing)
win_b1.grid(row=2, column=1, padx=5, pady=5)

win.mainloop()
