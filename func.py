import os
import sys
import win32api
import time
import pyautogui as pg
import pytesseract as pt
import pyperclip as cp
import tkinter as tk
import threading
import cv2
from PIL import Image

def screenshot(start, end):
    myconfig = r"--psm 6 --oem 3" #10
    str = len(start)
    ed = len(end)
    if str == 2 and ed == 2:
        distx = end[0] - start[0]
        disty = end[1] - start[1]
        ss = pg.screenshot(region=(start[0], start[1], distx, disty))
        ss.save("ss.png")
        
        ss= cv2.imread("ss.png")
        ss = cv2.cvtColor(ss, cv2.COLOR_BGR2GRAY)
        text = pt.image_to_string(ss, config=myconfig)
        print(text)
        cp.copy(text)
        os._exit(1)
    
def task():
    print("gg")
    running = True


    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)
    print(height,width)
    midWidth = int((width + 1) / 2)
    midHeight = int((height + 1) / 2)



    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    print("start")
    while True:
        print("loop")
        a = win32api.GetKeyState(0x01)
        #print(a)
        if a != state_left:  # Button state changed
            state_left = a
            print(a)
            try:
                if a == -127 or a == -128:
                    pos_start = pg.position()
                    print(pos_start)
                    print('Left Button Pressed')
                else:
                    
                    print('Left Button Released')
                    pos_end = pg.position()
                    screenshot(pos_start, pos_end)
            except SystemError:
                continue
                #win32api.SetCursorPos((midWidth, midHeight))
        time.sleep(0.001)
        
root = tk.Tk()
root.geometry("1366x768")
root.attributes("-alpha", 0.1)
try:
    root.config(cursor="" + "cross")
except tk.TclError:
    pass

#myCanvas = tk.Frame(root, bg="red", height=768, width=1366,cursor="@cross.cur",)
#myCanvas.place(anchor="ne", x=0, y=0)
thread = threading.Thread(target=task)   
thread.start()

tk.mainloop()