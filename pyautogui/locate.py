import pyautogui as pg
from time import sleep
pg.leftClick(x=781, y=68)
sleep(1)
print(pg.locateOnScreen('sc.png'))