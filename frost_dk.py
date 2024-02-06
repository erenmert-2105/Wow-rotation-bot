import win32api
import time 
import numpy as np
import mss
import mss.tools
import pyautogui
import warnings
import cv2
import random
import pyttsx3

# filter warnings
warnings.filterwarnings('ignore')


def Random():
    r1 = random.uniform(0.3, 0.1)
    return round(r1, 2)


def Obli():
    pyautogui.press('2')
def Frostst():
    pyautogui.press('3')
def Rime():
    pyautogui.press('1')
def Winter():
    pyautogui.press('5')

engine = pyttsx3.init()    
engine.setProperty('rate', 200)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)



a=win32api.GetKeyState(192)
b=a

froststrike = cv2.imread('Frost/1,10-34,35_frostst.png', cv2.TM_CCOEFF_NORMED)
froststrike2 = cv2.imread('Frost/0,90-34,35_frostst2.png', cv2.TM_CCOEFF_NORMED)
obli = cv2.imread('Frost/42,10-34,35_obli.png', cv2.TM_CCOEFF_NORMED)
rime = cv2.imread('Frost/42,50-34,35_rime.png', cv2.TM_CCOEFF_NORMED)
winter = cv2.imread('Frost/90,50-34,35_winter.png', cv2.TM_CCOEFF_NORMED)
killing_machine = cv2.imread('Frost/1,50-34,35_killingmachine.png', cv2.TM_CCOEFF_NORMED)
fight = cv2.imread('Frost/91,9-34,35_fight.png', cv2.TM_CCOEFF_NORMED)


state = 2
state_ =2

engine.say("Press tilda button to start frost bot")
engine.runAndWait()

while True:
    a=win32api.GetKeyState(192)
    
    if state==1 and state_==2:
        engine.say("bot is activated")
        engine.runAndWait()
    elif state==2 and state_==1:
        engine.say("bot is deeeactivated")
        engine.runAndWait()
        
    state_=state
    

    if b != a:
        state=1
        # main code here
        
        # Define the regions to capture
        regions = [
            {"left": 1, "top": 10, "width": 34, "height": 35},
            {"left": 0, "top": 90, "width": 34, "height": 35},
            {"left": 42, "top": 10, "width": 34, "height": 35},
            {"left": 42, "top": 50, "width": 34, "height": 35},
            {"left": 90, "top": 50, "width": 34, "height": 35},
            {"left": 91, "top": 9, "width": 34, "height": 35},
            {"left": 1, "top": 50, "width": 34, "height": 35}
        ]
        
        captured_images = []
        
        
        with mss.mss() as sct:
            for i, region in enumerate(regions):
                # Capture a screenshot of the specified region
                screenshot = sct.grab(region)
        
                # Convert the screenshot to a NumPy array without the alpha channel
                img_array = np.array(screenshot.pixels, dtype=np.uint8)[:,:,:3]
        
                # Append the image array to the list
                captured_images.append(img_array)
                
        
        imfroststrike= captured_images[0]
        imfroststrike2= captured_images[1]
        imobli= captured_images[2]
        imrime=  captured_images[3]
        imwinter=  captured_images[4]
        imfight= captured_images[5]
        imkilling_machine= captured_images[6]


        
        resultfroststrike = cv2.matchTemplate(imfroststrike, froststrike, cv2.TM_CCOEFF_NORMED)
        min_val, max_valfroststrike, min_loc, max_loc = cv2.minMaxLoc(resultfroststrike)
        
        resultfroststrike2 = cv2.matchTemplate(imfroststrike2, froststrike2, cv2.TM_CCOEFF_NORMED)
        min_val, max_valfroststrike2, min_loc, max_loc = cv2.minMaxLoc(resultfroststrike2)
        
        resultobli = cv2.matchTemplate(imobli, obli, cv2.TM_CCOEFF_NORMED)
        min_val, max_valobli, min_loc, max_loc = cv2.minMaxLoc(resultobli)
        
        resultrime = cv2.matchTemplate(imrime, rime, cv2.TM_CCOEFF_NORMED)
        min_val, max_valrime, min_loc, max_loc = cv2.minMaxLoc(resultrime) 
        
        resultwinter = cv2.matchTemplate(imwinter, winter, cv2.TM_CCOEFF_NORMED)
        min_val, max_valwinter, min_loc, max_loc = cv2.minMaxLoc(resultwinter)      
        
        resultfight = cv2.matchTemplate(imfight, fight, cv2.TM_CCOEFF_NORMED)
        min_val, max_valfight, min_loc, max_loc = cv2.minMaxLoc(resultfight)     
        
        resultkilling_machine = cv2.matchTemplate(imkilling_machine, killing_machine, cv2.TM_CCOEFF_NORMED)
        min_val, max_valkilling_machine, min_loc, max_loc = cv2.minMaxLoc(resultkilling_machine)           
        


        if max_valfight >0.7:
            if max_valwinter > 0.7:
                Winter()
            else:
                if max_valfroststrike2 > 0.7:
                    Frostst()
                else:
                    if  max_valrime > 0.65:
                        Rime()
                    else:
                        if resultkilling_machine >0.7:
                            Obli()
                        else:
                            if max_valfroststrike > 0.7:
                                Frostst()
                            else:
                                if max_valobli > 0.7:
                                    Obli()                  
            
        
        
        
        
    else:
        time.sleep(0.1)
        state=2
