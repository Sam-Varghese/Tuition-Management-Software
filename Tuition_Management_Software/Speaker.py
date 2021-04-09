# This file contains program for speaking

import win32api
import pyttsx3

def speaking(text):
    
    engine=pyttsx3.init()
    engine.say(text)
    engine.setProperty('rate',125)
    engine.setProperty('volume',1)
    engine.runAndWait()