from itertools import count
import pyautogui
import time
time.sleep(4)
count=1
while count<=5:
    pyautogui.typewrite("Happy Diwali"+str(count))
    pyautogui.press("enter")
    count=count+1
   