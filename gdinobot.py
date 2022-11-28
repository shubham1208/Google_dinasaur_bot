import pyautogui
import time
import keyboard


time.sleep(3)
while True:
    im = pyautogui.screenshot()
    screen = im.getpixel((572, 685))
    x1 = im.getpixel((453, 655))
    x2 = im.getpixel((480, 655))
    x3 = im.getpixel((480, 655))
    x4 = im.getpixel((480, 655))

    y1 = im.getpixel((572, 685))
    y2 = im.getpixel((572, 685))
    y3 = im.getpixel((572, 685))
    y4 = im.getpixel((572, 685))

    if screen[0] == 32:
        if x1[0] != 32 or x2[0] != 32 or x3[0] != 32 or x4[0] != 32:
            pyautogui.press('space')
            time.sleep(0.001)
    else:
        if x1[0] != 32 or x2[0] != 32 or x3[0] != 32 or x4[0] != 32:
            pyautogui.press('space')
            time.sleep(0.001)

    if keyboard.is_pressed("space"):
        break