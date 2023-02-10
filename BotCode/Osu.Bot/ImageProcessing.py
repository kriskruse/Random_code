import numpy as np
import cv2
import pyautogui


# Function that graps screen of process and retuns it as a numpy array
def grab_screen(region=None):
    screen = np.array(pyautogui.screenshot(region=region))
    return cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
