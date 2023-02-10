import numpy as np
import cv2
import pyautogui
import dxcam
import mss


# Function that graps screen of process and retuns it as a numpy array
def autoguiCapture(region=None):
    screen = np.array(pyautogui.screenshot(region=region))
    return cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

def dxCamCapture():
    camera = dxcam.create()
    frame = camera.grab()
    return frame

def mssCapture():
    with mss.mss() as sct:
        monitor = {"top": 0 , "left": 0, "width": 1920, "height": 1080}
        img_array = np.array(sct.grab(monitor))
        return img_array