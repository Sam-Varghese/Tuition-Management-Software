# This file contains program to open GeoGebra apps

# Importing necessary libraries
print('Importing necessary libraries...')
from tkinter import *
from tkinter import ttk
from Classes import *
import webbrowser
import threading
import time

def geogebra():
    
    # Making the main geogebra window
    
    geo_win=Tk()
    geo_win_gui=window(geo_win, 'GeoGebra')
    
    geo_win_lf1=LabelFrame(geo_win, text='GeoGebra Apps', relief='groove', bd=10)
    geo_win_lf1.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    
    # Making button for Calculator Suite
    
    def geo_win_b1_func():
        
        webbrowser.open('https://www.geogebra.org/calculator')
        
    
    geo_win_b1=ttk.Button(geo_win_lf1, text='Calculator Suite',command= geo_win_b1_func)
    geo_win_b1.grid(row=0, column=0, padx=5, pady=5)
    
    # Making button for 3D Calculator 
    
    def geo_win_b2_func():
        
        webbrowser.open('https://www.geogebra.org/3d')
        
    
    geo_win_b2=ttk.Button(geo_win_lf1, text='3D Calculator', command=geo_win_b2_func)
    geo_win_b2.grid(row=0, column=1, padx=5, pady=5)
    
    # Making button for CAS Calculator
    
    def geo_win_b3_func():
        
        webbrowser.open('https://www.geogebra.org/cas')
        
    
    geo_win_b3=ttk.Button(geo_win_lf1, text='CAS Calculator', command=geo_win_b3_func)
    geo_win_b3.grid(row=0, column=2, padx=5, pady=5)
    
    # Making button for Geometry
    
    def geo_win_b4_func():
        
        webbrowser.open('https://www.geogebra.org/geometry')
        
    
    geo_win_b4=ttk.Button(geo_win_lf1, text='Geometry', command=geo_win_b4_func)
    geo_win_b4.grid(row=1, column=0, padx=5, pady=5)
    
    # Making button for Graphing Calculator
    
    def geo_win_b5_func():
        
        webbrowser.open('https://www.geogebra.org/graphing')
        
    
    geo_win_b5=ttk.Button(geo_win_lf1, text='Graphing Calculator', command=geo_win_b5_func)
    geo_win_b5.grid(row=1, column=1, padx=5, pady=5)
    
    # Making button for Scientific Calculator
    
    def geo_win_b5_func():
        
        webbrowser.open('https://www.geogebra.org/scientific')
        
    
    geo_win_b6 = ttk.Button(
        geo_win_lf1, text='Scientific Calculator', command=geo_win_b5_func)
    geo_win_b6.grid(row=1, column=2, padx=5, pady=5)

    # Making button for GeoGebra Classic
    
    def geo_win_b7_func():
        
        webbrowser.open('https://www.geogebra.org/classic')
        

    geo_win_b7 = ttk.Button(
        geo_win_lf1, text='GeoGebra Classic', command=geo_win_b7_func)
    geo_win_b7.grid(row=2, column=0, padx=5, pady=5)
 
    # Making button for Testing
    
    def geo_win_b8_func():
        
        webbrowser.open('https://www.geogebra.org/m/y3aufmy8')
        

    geo_win_b8 = ttk.Button(
        geo_win_lf1, text='Testing', command=geo_win_b8_func)
    geo_win_b8.grid(row=2, column=1, padx=5, pady=5)
    
    # Making button for Notes
    
    def geo_win_b9_func():
        
        webbrowser.open('https://www.geogebra.org/notes')
        

    geo_win_b9 = ttk.Button(
        geo_win_lf1, text='Notes', command=geo_win_b9_func)
    geo_win_b9.grid(row=2, column=2, padx=5, pady=5)

    geo_win.mainloop()
