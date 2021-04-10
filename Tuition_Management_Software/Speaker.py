# This file contains program for speaking

import win32api
import pyttsx3

def speaking(text):
        
    pyttsx3.speak(text)
