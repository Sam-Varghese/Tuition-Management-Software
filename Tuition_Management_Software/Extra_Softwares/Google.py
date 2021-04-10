# This file contains program which can make teacher directly go to google (using webbrowser module)

# Importing necessary libraries
print('Importing necessary libraries for google button...')
import threading
import time
from Classes import *
import webbrowser
from tkinter import ttk
from tkinter import *
lock = threading.Lock()


def speak(text, lock=lock):  # put thread locking as speak fuctions simultaneously executing produces errors

    def process(text, lock):
        from Speaker import speaking
        lock.acquire()
        speaking(text)
        lock.release()

    threading.Thread(target=process, args=(text, lock)).start()


def google_window():

    # Necessary because speaking 'opening google' would generate error as speaking statements of this program would do collisions
    time.sleep(3)
    # Making window...
    print('Making google window...')
    google_win = Tk()
    google_win_gui = window(google_win, 'Google')

    google_win_lf1 = LabelFrame(google_win, text='Google Apps')
    google_win_lf1.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    # Google Chrome button

    def google_win_b1_function():
        speak('Opening google chrome sir')

    google_win_b1 = ttk.Button(
        google_win_lf1, text='Google-Chrome', command=google_win_b1_function)
    google_win_b1.grid(row=0, column=0, padx=5, pady=5)

    # Google Meet button

    def google_win_b2_function():
        speak('Opening google meet sir')

    google_win_b2 = ttk.Button(
        google_win_lf1, text='Google-Meet', command=google_win_b2_function)
    google_win_b2.grid(row=0, column=1, padx=5, pady=5)

    # Google Classroom button

    def google_win_b3_function():
        speak('Opening google classroom sir')

    google_win_b3 = ttk.Button(
        google_win_lf1, text='Google-Classroom', command=google_win_b3_function)
    google_win_b3.grid(row=0, column=2, padx=5, pady=5)

    # G-Mail button

    def google_win_b4_function():
        speak('Opening gmail sir')

    google_win_b4 = ttk.Button(
        google_win_lf1, text='G Mail', command=google_win_b4_function)
    google_win_b4.grid(row=0, column=3, padx=5, pady=5)

    # Google Sheets button

    def google_win_b5_function():
        speak('Opening google sheets sir')

    google_win_b5 = ttk.Button(
        google_win_lf1, text='Google-Sheets', command=google_win_b5_function)
    google_win_b5.grid(row=1, column=0, padx=5, pady=5)

    # Google photos button

    def google_win_b6_function():
        speak('Opening google photos sir')

    google_win_b6 = ttk.Button(
        google_win_lf1, text='Google-Photos', command=google_win_b6_function)
    google_win_b6.grid(row=1, column=1, padx=5, pady=5)

    # Google Maps button

    def google_win_b7_function():
        speak('Opening google maps sir')

    google_win_b7 = ttk.Button(
        google_win_lf1, text='Google-Maps', command=google_win_b7_function)
    google_win_b7.grid(row=1, column=2, padx=5, pady=5)

    # Google Forms button

    def google_win_b8():
        speak('Opening google forms sir')

    google_win_b8 = ttk.Button(
        google_win_lf1, text='Google-Forms', command=google_win_b8)
    google_win_b8.grid(row=1, column=3, padx=5, pady=5)

    # Google calendar button

    def google_win_b9():
        speak('Opening google calendar')

    google_win_b9 = ttk.Button(
        google_win_lf1, text='Google-Calendar', command=google_win_b9)
    google_win_b9.grid(row=2, column=0, padx=5, pady=5)

    # Google Docs button

    def google_win_b10():
        speak('Opening google docs sir')

    google_win_b10 = ttk.Button(
        google_win_lf1, text='Google-Docs', command=google_win_b10)
    google_win_b10.grid(row=2, column=1, padx=5, pady=5)

    # Google Slides button

    def google_win_b11():
        speak('Opening google slides sir')

    google_win_b11 = ttk.Button(
        google_win_lf1, text='Google-Slides', command=google_win_b11)
    google_win_b11.grid(row=2, column=2, padx=5, pady=5)

    # Google Drive button

    def google_win_b12():
        speak('Opening google drive')

    google_win_b12 = ttk.Button(
        google_win_lf1, text='Google-Drive', command=google_win_b12)
    google_win_b12.grid(row=2, column=3, padx=5, pady=5)

    google_win.mainloop()
