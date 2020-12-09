import pyautogui
import time
import keyboard

x = 0
word = input ("watto spam: ")

time.sleep(5)

while True:
    pyautogui.typewrite(word)

    pyautogui.press("enter")
    x = x + 1
    if keyboard.is_pressed('esc'):
        print('\"',word, '\"', " x ", x, sep="")
        break
