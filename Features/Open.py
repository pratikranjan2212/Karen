import os
import webbrowser
import pyautogui
import keyboard
from time import sleep

def OpenExe(Query):
    Query = str(Query).lower()

    if 'visit' in Query:
        nameofweb = Query.replace('visit ','')
        Link = f"https://www.{nameofweb}.com"
        webbrowser.open(Link)
        return True
        
    elif 'open' in Query:
        nameofapp = Query.replace('open ','')
        pyautogui.press('win')
        sleep(1)
        keyboard.write(nameofapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    
    elif 'launch' in Query:
        nameofapp = Query.replace('launch ','')
        pyautogui.press('win')
        sleep(1)
        keyboard.write(nameofapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    
    elif 'start' in Query:
        nameofapp = Query.replace('start ','')
        if 'word' in nameofapp or 'ms word' in nameofapp or 'microsoft word' in nameofapp:
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD")
            return True

OpenExe('open spotify')