
import pyautogui as py
import time

time.sleep(1)
#print(py.position())

py.moveTo(26,1079)
time.sleep(1)
py.leftClick()
time.sleep(1)
py.typewrite("edge")
time.sleep(1)
py.press("enter")
time.sleep(1)
py.typewrite("https://web.whatsapp.com")
time.sleep(1)
py.press("enter")
time.sleep(1)
py.moveTo(430,196)
time.sleep(20)
py.leftClick()
py.typewrite("balaji")
time.sleep(1)
py.press("enter")
time.sleep(1)
for i in range(10):
    py.typewrite("hi")
    time.sleep(1)
    py.press("enter")

