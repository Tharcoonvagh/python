import keyboard
import pyautogui

print(pyautogui.position())

while True:
    print(pyautogui.position())
    if keyboard.is_pressed("esc"):
        break
