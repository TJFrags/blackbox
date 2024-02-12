from time import time
import pyautogui as pg
import time
time.sleep(2)
ss = pg.screenshot(region=(500,500,10,5))
ss.show()