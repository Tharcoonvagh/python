import subprocess
import keyboard
import pyautogui
import time
x = input("Mit spammeljek az ismerősödnek? ")
count = 1
subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe")
pyautogui.click(81, 360)
pyautogui.click(858, 730)
while count == 1:
   keyboard.write(x)
   keyboard.press("enter")
   if keyboard.is_pressed("esc"):
      break

##pyautogui.keyDown("alt")
##pyautogui.press("tab")
##pyautogui.keyUp("alt")
