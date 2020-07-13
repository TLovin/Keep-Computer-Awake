# This code moves the mouse at set time intervals to prevent computer from sleeping

import pyautogui
import random
import time


class PreventSleep:
    def _movemouserandomly(w, h):
        x = random.randint(0, w)
        y = random.randint(0, h)
        pyautogui.moveTo(x, y, duration=0.5)

    def preventsleep(sec):
        w, h = pyautogui.size()

        while True:
            PreventSleep._movemouserandomly(w, h)
            time.sleep(sec)


PreventSleep.preventsleep(300)



