import pyautogui
import time
import mouse
import keyboard
import random
bylo = 2
prohod = 0
proeb = 0
while True:
            time.sleep(1)
            if keyboard.is_pressed('e'):
                break
while True:
    color = pyautogui.pixel(747, 958)
    if color[0] == 168:
        time.sleep(2.5)
        bylo = 1
    elif color[0] == 92:
        mouse.click('left')
        if bylo == 1:
            bylo = 2
    else:
        if bylo == 2:
            if prohod == 20:
                keyboard.press("w")
                time.sleep(0.3)
                keyboard.release("w")
            elif prohod == 40:
                keyboard.press("s")
                time.sleep(0.3)
                keyboard.release("s")
                prohod = 0
            time.sleep(random.randint(1, 2)+random.random())
            keyboard.press("4")
            time.sleep(0.5)
            keyboard.release("4")
            proeb = 0
            bylo = 0
            prohod += 1
            
        else:
            if proeb > 45:
                keyboard.press("4")
                time.sleep(0.5)
                keyboard.release("4")
                proeb = 0
            else:
                time.sleep(0.5)
                proeb += 1
    if keyboard.is_pressed('q'):
        while True:
            time.sleep(1)
            if keyboard.is_pressed('e'):
                break
