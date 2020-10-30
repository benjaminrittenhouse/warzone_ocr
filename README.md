# warzone_ocr
Python OCR that sends a message (or types a message and clicks enter) for any time the user is in the top 10 of Warzone. This code uses pytesseract OCR and captures the part of the screen that shows how many people are left in the game. If it is below 10, use pyautogui to write a message and send it.
