import pyscreenshot as ImageGrab
from PIL import Image 
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

path="C:/Users/erenm/OneDrive/Masaüstü/wow_Rotation _Bot/"
method = cv2.TM_CCOEFF_NORMED
# filter warnings
warnings.filterwarnings('ignore')


def Random():
    r1 = random.uniform(0, 0.1)
    return round(r1, 2)


def Barbed():
    pyautogui.press('8')
def Kcommand():
    pyautogui.press('1')
def Cleave():
    pyautogui.press('5')
def Chakram():
    pyautogui.press('9')
def Cobrashot():
    pyautogui.press('4')
def Mark():
    pyautogui.press('7')    
def Kshot():
    pyautogui.press('6')      


engine = pyttsx3.init()    
engine.setProperty('rate', 200)  # Speed of speech
engine.setProperty('volume', 0.5)  # Volume (0.0 to 1.0)



a=win32api.GetKeyState(192)
b=a


barbed_count = np.array(Image.open("C:/Users/erenm/OneDrive/Masaüstü/wow_Rotation _Bot/Images/Barbed_cound.png"))
barbed = np.array(Image.open("C:/Users/erenm/OneDrive/Masaüstü/wow_Rotation _Bot/Images/Barbed.png"))
killcommand = np.array(Image.open("C:/Users/erenm/OneDrive/Masaüstü/wow_Rotation _Bot/Images/Killcommend.png"))
cleave = np.array(Image.open("C:/Users/erenm/OneDrive/Masaüstü/wow_Rotation _Bot/Images/Aoe_bm.png"))
combat = np.array(Image.open("C:/Users/erenm/OneDrive/Masaüstü/wow_Rotation _Bot/Images/Combat_bm.png"))
fdeath = np.array(Image.open("C:/Users/erenm/OneDrive/Masaüstü/wow_Rotation _Bot/Images/Fdead.png"))
killshot = np.array(Image.open("C:/Users/erenm/OneDrive/Masaüstü/wow_Rotation _Bot/Images/Kshot.png"))
mark = np.array(Image.open("C:/Users/erenm/OneDrive/Masaüstü/wow_Rotation _Bot/Images/Mark.png"))
cobrashot = np.array(Image.open("C:/Users/erenm/OneDrive/Masaüstü/wow_Rotation _Bot/Images/Cobrashot.png"))
chakram = np.array(Image.open("C:/Users/erenm/OneDrive/Masaüstü/wow_Rotation _Bot/Images/Chakram.png"))    



state = 2
state_ =2

engine.say("Press tilda button to start bm bot")
engine.runAndWait()

while True:
    time.sleep(Random())
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
            {"left": 12, "top": 10, "width": 29, "height": 29},
            {"left": 45, "top": 10, "width": 29, "height": 29},
            {"left": 78, "top": 10, "width": 29, "height": 29},
            {"left": 109, "top": 10, "width": 29, "height": 29},
            {"left": 143, "top": 12, "width": 29, "height": 29},
            {"left": 12, "top": 42, "width": 29, "height": 29},
            {"left": 44, "top": 42, "width": 29, "height": 29},
            {"left": 75, "top": 42, "width": 29, "height": 29},
            {"left": 109, "top": 42, "width": 29, "height": 29},
            {"left": 142, "top": 43, "width": 29, "height": 29}
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
                
        Cbarbed_count= captured_images[0]
        Cbarbed= captured_images[1]
        Ckillcommand =  captured_images[2]
        Ccleave =  captured_images[3]
        Ccombat=  captured_images[4]
        Cchakram= captured_images[5]
        Ccobrashot= captured_images[6]
        Cmark= captured_images[7]
        Cfdeath= captured_images[8]
        Ckshot=  captured_images[9]

        



        Rbarbed_count = cv2.matchTemplate(barbed_count, Cbarbed_count, method)
        
        Rbarbed = cv2.matchTemplate(barbed, Cbarbed, method)
        
        Rkillcommand = cv2.matchTemplate(killcommand, Ckillcommand, method)
        
        Rcleave = cv2.matchTemplate(cleave, Ccleave, method)
        
        Rcombat = cv2.matchTemplate(combat, Ccombat, method)
        
        Rchakram = cv2.matchTemplate(chakram, Cchakram, method)
        
        Rcobrashot = cv2.matchTemplate(cobrashot, Ccobrashot, method)
        
        Rmark = cv2.matchTemplate(mark, Cmark, method)
        
        Rfdeath = cv2.matchTemplate(fdeath, Cfdeath, method)
        
        Rkshot = cv2.matchTemplate(killshot, Ckshot, method)
        
        
        if Rcombat > 0.65:
            if Rfdeath < 0.7:
                if Rmark >0.7:
                    Mark()
                    
                elif Rcleave >0.7:
                    Cleave()
                    
                elif Rbarbed_count > 0.7 and Rbarbed >0.7:
                    Barbed()   
                    
                elif Rkshot > 0.7:
                    Kshot()                   
                    
                elif Rkillcommand >0.7:
                    Kcommand()
                    
                elif Rchakram >0.7:
                    Chakram()
                    
                elif Rcobrashot >0.7:
                    Cobrashot()
                    
                    
                    
    else:
        state=2
                
                
















