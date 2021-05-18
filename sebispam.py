import pyautogui
import time
import keyboard

x = 0
word = input ("watto spam: ")

time.sleep(5)

while True:
    if keyboard.is_pressed('esc'):
        print('\"',word, '\"', " x ", x, sep="")
        break
    else:
        pyautogui.typewrite(word)

        pyautogui.press("enter")
        x = x + 1
        
