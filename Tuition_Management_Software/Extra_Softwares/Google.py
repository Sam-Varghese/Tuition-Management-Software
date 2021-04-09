# This file contains program which can make teacher directly go to google (using webbrowser module)

# Importing necessary libraries
print('Importing necessary libraries for google button...')
from tkinter import *
from tkinter import ttk
import webbrowser
from Classes import *

def google_window():
    
    # Making window...
    print('Making google window...')
    google_win=Tk()
    google_win_gui=window(google_win, 'Google')
    
    google_win_lf1=LabelFrame(google_win, text='Google Apps')
    google_win_lf1.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
    
    # Google Chrome button
    
    google_win_b1=ttk.Button(google_win_lf1, text='Google-Chrome')
    google_win_b1.grid(row=0,column=0,padx=5,pady=5)
    
    # Google Meet button
    
    google_win_b2=ttk.Button(google_win_lf1, text='Google-Meet')
    google_win_b2.grid(row=0,column=1,padx=5,pady=5)
    
    # Google Classroom button
    
    google_win_b3=ttk.Button(google_win_lf1, text='Google-Classroom')
    google_win_b3.grid(row=0, column=2, padx=5, pady=5)
    
    # G-Mail button
    
    google_win_b4=ttk.Button(google_win_lf1, text='G Mail')
    google_win_b4.grid(row=0, column=3, padx=5, pady=5)
    
    # Google Sheets button
    
    google_win_b5=ttk.Button(google_win_lf1, text='Google-Sheets')
    google_win_b5.grid(row=1, column=0, padx=5, pady=5)
    
    # Google photos button
    
    google_win_b6=ttk.Button(google_win_lf1, text='Google-Photos')
    google_win_b6.grid(row=1, column=1, padx=5, pady=5)
    
    # Google Maps button
    
    google_win_b7=ttk.Button(google_win_lf1, text='Google-Maps')
    google_win_b7.grid(row=1,column=2, padx=5, pady=5)
    
    # Google Forms button
    
    google_win_b8=ttk.Button(google_win_lf1, text='Google-Forms')
    google_win_b8.grid(row=1,column=3,padx=5,pady=5)
    
    # Google calendar button
    
    google_win_b9=ttk.Button(google_win_lf1, text='Google-Calendar')
    google_win_b9.grid(row=2,column=0,padx=5,pady=5)
    
    # Google Docs button
    
    google_win_b10=ttk.Button(google_win_lf1, text='Google-Docs')
    google_win_b10.grid(row=2,column=1,padx=5,pady=5)
    
    # Google Slides button
    
    google_win_b11=ttk.Button(google_win_lf1, text='Google-Slides')
    google_win_b11.grid(row=2,column=2,padx=5,pady=5)
    
    # Google Drive button
    
    google_win_b12=ttk.Button(google_win_lf1, text='Google-Drive')
    google_win_b12.grid(row=2,column=3,padx=5,pady=5)
    
    google_win.mainloop()