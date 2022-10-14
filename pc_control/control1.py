from pynput import mouse
from pynput import keyboard
import time
import win32api, win32con


def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['æ', 'ø', 'å', 'right']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        print('Key pressed: ' + k)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0,100,0,0)
        # mo.move(200, 200,absolute=False, duration=0.2)

        # return False  # stop listener; remove this if want more keys
def on_press_mouse(x,y,key,pressed):
    print(key)
    if key == 'left':
        print('Key pressed: ' + key)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 100, 0, 0)

if __name__ == "__main__":
    mouse_lis = mouse.Listener(on_click=on_press_mouse)
    listener = keyboard.Listener(on_press=on_press)
    mouse_lis.start()
    listener.start()  # start to listen on a separate thread
    mouse_lis.join()
    listener.join()  # remove if main thread is polling self.keys

