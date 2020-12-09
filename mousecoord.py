import time
import keyboard
import pyautogui

#time.sleep(3)
print(pyautogui.position())
#pyautogui.click(pyautogui.position())

while True:
    print(pyautogui.position())
    if keyboard.is_pressed("esc"):
        break
