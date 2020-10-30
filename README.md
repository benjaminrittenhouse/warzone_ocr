# warzone_ocr
Python OCR that sends a message (or types a message and clicks enter) for any time the user is in the top 10 of Warzone. This code uses pytesseract OCR and captures the part of the screen that shows how many people are left in the game. If it is below 10, use pyautogui to write a message and send it.

Thing to know:
#pyautogui
1. pyautogui module uses the keyboard to write and send things. In order for these messages to send, you will need to have your cursor selected inside message window on discord, imessage, etc.
2. Once the program is running you cannot change where the cursor is. Wherever the cursor is, the message will write

#pytesseract
Pytesseract is the OCR module that is being used to capture the part of the screen that shows how many people are left in a warzone game. In the code, if you want to see which part of the image specifically is being captured, see line 59: cap = ImageGrab.grab(bbox =(1665, 30, 1755, 100)). The coordinates are the top left x, top y, bottom right x, bottom y. 

To show the image, type cap.show()

#Important
Run warzone in full screen on main monitor. An effective way to do this is mirror Xbox One to windows and run program so the mouse does not need to move (player is playing on xbox). Or, you can mirror the gameplay to a MacOS device that has a messaging app and remote access it. This would be where you put your mouse cursor so you can send messages via iMessage and let friends know when you are top 10 in Warzone. 

The winning screen is broken (see commented line 66 in war.py). Feel free to experiment with this code and try to get it to work more effeciently, more comments in the code about how it works!
