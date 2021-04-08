# This file contains program to open GeoGebra apps

# Importing necessary libraries
print('Importing necessary libraries...')
from tkinter import *
from tkinter import ttk
from Classes import *
import webbrowser

def geogebra():
    
    # Making the main geogebra window
    
    geo_win=Tk()
    geo_win_gui=window(geo_win, 'GeoGebra')
    
    geo_win_lf1=LabelFrame(geo_win, text='GeoGebra Apps')
    geo_win_lf1.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
    
    # Making button for Calculator Suite
    
    geo_win_b1=ttk.Button(geo_win_lf1, text='Calculator Suite', cursor='wait')
    geo_win_b1.grid(row=0, column=0, padx=5, pady=5)
    
    # Making button for 3D Calculator 
    
    geo_win_b2=ttk.Button(geo_win_lf1, text='3D Calculator', cursor='wait')
    geo_win_b2.grid(row=0, column=1, padx=5, pady=5)
    
    # Making button for CAS Calculator
    
    geo_win_b3=ttk.Button(geo_win_lf1, text='CAS Calculator', cursor='wait')
    geo_win_b3.grid(row=0, column=2, padx=5, pady=5)
    
    # Making button for Geometry
    
    geo_win_b4=ttk.Button(geo_win_lf1, text='Geometry', cursor='wait')
    geo_win_b4.grid(row=1, column=0, padx=5, pady=5)
    
    # Making button for Graphing Calculator
    
    geo_win_b5=ttk.Button(geo_win_lf1, text='Graphing Calculator', cursor='wait')
    geo_win_b5.grid(row=1, column=1, padx=5, pady=5)
    
    # Making button for Scientific Calculator
    
    geo_win_b6 = ttk.Button(
        geo_win_lf1, text='Scientific Calculator', cursor='wait')
    geo_win_b6.grid(row=1, column=2, padx=5, pady=5)

    # Making button for GeoGebra Classic

    geo_win_b7 = ttk.Button(
        geo_win_lf1, text='GeoGebra Classic', cursor='wait')
    geo_win_b7.grid(row=2, column=0, padx=5, pady=5)
 
    # Making button for Testing

    geo_win_b8 = ttk.Button(
        geo_win_lf1, text='Testing', cursor='wait')
    geo_win_b8.grid(row=2, column=1, padx=5, pady=5)
    
    # Making button for Notes

    geo_win_b9 = ttk.Button(
        geo_win_lf1, text='Notes', cursor='wait')
    geo_win_b9.grid(row=2, column=2, padx=5, pady=5)

    geo_win.mainloop()