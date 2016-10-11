"""
Some basic automation of mouse and keyboard
"""

import pyautogui
import time

print(pyautogui.size())  # information about the screen size
print(pyautogui.position())  # information about the current position of the mouse pointer

# Section to open the browser, open the new tab and go to github website
pyautogui.click(77, 1066, button='left', duration=0.25)
time.sleep(5)
pyautogui.hotkey('ctrl', 't')
time.sleep(2)
pyautogui.typewrite('http://www.github.com\n')


# Some other code not used
#pyautogui.click(10, 183, button='left', duration=0.1)

#pyautogui.click(555, 270); pyautogui.typewrite('Hello world!\n')
