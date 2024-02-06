import pyscreenshot as ImageGrab
import win32api
import time 
import mss
import mss.tools
import numpy as np
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


def Aura():
    pyautogui.press('9')
def Spike():
    pyautogui.press('8')
def Fructure():
    pyautogui.press('6')
def Cleave():
    pyautogui.press('7')

engine = pyttsx3.init()    
engine.setProperty('rate', 200)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)



a=win32api.GetKeyState(192)
b=a

aura = cv2.imread('Vengance/51,9-35,36_aura.png', cv2.TM_CCOEFF_NORMED)
spike = cv2.imread('Vengance/10,9-35,36_spike.png', cv2.TM_CCOEFF_NORMED)
cleave = cv2.imread('Vengance/50,49-35,36_cleave.png', cv2.TM_CCOEFF_NORMED)
fructure = cv2.imread('Vengance/11,50-35,36_frugcture.png', cv2.TM_CCOEFF_NORMED)
combat = cv2.imread('Vengance/91,9-35,36_combat.png', cv2.TM_CCOEFF_NORMED)


state = 2
state_ =2

engine.say("Press tilda button to start vengance bot")
engine.runAndWait()

while True:
    time.sleep(0.1)
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
            {"left": 51, "top": 9, "width": 35, "height": 36},
            {"left": 10, "top": 9, "width": 35, "height": 36},
            {"left": 50, "top": 49, "width": 35, "height": 36},
            {"left": 11, "top": 50, "width": 35, "height": 36},
            {"left": 91, "top": 9, "width": 35, "height": 36},
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
                
        imaura= captured_images[0]
        imspike= captured_images[1]
        imcleave=  captured_images[2]
        imfracture=  captured_images[3]
        imcombat= captured_images[4]


        
        resultaura = cv2.matchTemplate(imaura, aura, cv2.TM_CCOEFF_NORMED)
        min_val, max_valaura, min_loc, max_loc = cv2.minMaxLoc(resultaura)
        
        resultspike = cv2.matchTemplate(imspike, spike, cv2.TM_CCOEFF_NORMED)
        min_val, max_valspike, min_loc, max_loc = cv2.minMaxLoc(resultspike)

        resultcleave = cv2.matchTemplate(imcleave, cleave, cv2.TM_CCOEFF_NORMED)
        min_val, max_valcleave, min_loc, max_loc = cv2.minMaxLoc(resultcleave)

        resultfracture = cv2.matchTemplate(imfracture, fructure, cv2.TM_CCOEFF_NORMED)
        min_val, max_valfracture, min_loc, max_loc = cv2.minMaxLoc(resultfracture)   
        
        resultcombat = cv2.matchTemplate(imcombat, combat, cv2.TM_CCOEFF_NORMED)
        min_val, max_valcombat, min_loc, max_loc = cv2.minMaxLoc(resultcombat)   
        
        
        
        
        if max_valcombat >0.7:
            if max_valaura > 0.7:
                Aura()
            else:
                if  max_valspike < 0.3:
                    Spike()
                else:
                    if max_valcleave > 0.7:
                        Cleave()
                    else:                  
                        if max_valfracture > 0.6:
                            Fructure()
        
        
        
        
        
    else:
        state=2
        
        
    
                      
      

    
    

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    