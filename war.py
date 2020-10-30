'''
@Author Benjamin Rittenhouse
@File war.py
Program that uses OCR Python module and captures part of the screen where total players left exists
Conver to string, use pyautogui to write to where cursor is
'''

#mumpy
import numpy as nm 
  
#pytesseract OCR
import pytesseract 

# pyautogui
import pyautogui
  
# importing OpenCV 
import cv2 
 
#pillow
from PIL import ImageGrab 
from PIL import ImageFilter
import PIL

# 150 players in warzone game
nums = []
for i in range(1, 151):
    nums.append(i)

# define the starting amount of players in the game
def startingPlace():
    place = None
    placeSet = False
    # ESTABLISH PATH TO TESSERACT OCR EXE
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    #while no place has been set
    while placeSet is False:
    	#set the place by screen grabbing where the place is displayed (top left)
        cap = ImageGrab.grab(bbox =(1675, 0, 1750, 100)) 
        # convert to string
        screen = pytesseract.image_to_string( 
                    cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),  
                    lang ='eng')
        try:
        	# if the value is included in nums (in case the value has a random non character from bad OCR read)
            if int(screen[1:len(screen)]) in nums:
            	# set value
                screen = int(screen[1:len(screen)])
                place = screen
                placeSet = True
        except:
            pass

    return place


# define converting the image to string and writing it with autogui
def imToString(): 
	#esetablish executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

   	#establish starting place 
    place = startingPlace()
    while(True): 
    	#grab top corner of screen to get place
        cap = ImageGrab.grab(bbox =(1665, 30, 1755, 100))
        #convert cap to string, "screen" is screen grab to string of current place
        screen = pytesseract.image_to_string( 
                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),  
                lang ='eng')


        # Capture part of screen where "Victory" is displayed and write message that they won ( NOT WORKING !)
        win = ImageGrab.grab(bbox =(1050, 800, 1500, 1000)) 
        winScreen = pytesseract.image_to_string( 
                cv2.cvtColor(nm.array(win), cv2.COLOR_BGR2GRAY),  
               lang ='eng')
        poss = ["victory!", "victory", "warzone victory", "warzone"]
        if winScreen.lower() in poss:
            pyautogui.write("User won Warzone!")
            pyautogui.press("enter")
            break
        ########################################################################################################
       

        try: # try to see if screen capture is an int and is within 1-150
            if int(screen[1:len(screen)]) in nums:
            	#set screen to this int
                screen = int(screen[1:len(screen)])
            else:
                pass
        except:
            pass
        
        # if screen is not in between 1 and 150
        if screen not in nums:
        	#do nothing
            pass
        else:
        	# screen is different than the place they are in (as in it changed) and screen did not change by more than 10 (to avoid jumps / OCR errors)
            if screen != place and abs(screen - (place + 1)) < 10:
            	# if screen value is in top 10 and is divisible by 2 (every 2 people that get eliminated in top 10, send message)
                if screen <= 10 and screen % 2 == 0:
                	# use pyautogui to write they are in the top num
                    pyautogui.write("User is top " + str(screen) + " in Warzone!") # place in warzone
                    #press enter (if user wants to have cursor in messages window to send message to someone that they are top x)
                    pyautogui.press("enter")
                    place = screen
                else:
                	#otherwise, update the place
                    place = screen
            elif screen == place:
                pass
        
  
# Calling the function 
imToString()
