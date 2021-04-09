import win32api
import pyttsx3

def speaking(text):
    
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()