import pyautogui
import time
i=0
# 10,11,12,13,14,15,16,17,18,19,20
# py,ja,py,ja,py,ja,py,ja,py,ja,py
# 5/2 => 2, 1
# 4/2 => 2, 0
# 4%2 = 0, 9%4 = 1
time.sleep(5)
pyautogui.typewrite("<=======================================================>")
pyautogui.press('enter')
while i<10:
    if i%2==0:
        pyautogui.typewrite("python")
        time.sleep(1) #wait for 3 sec
        pyautogui.press('enter')
    else:
        pyautogui.typewrite("java")
        time.sleep(3)  # wait for 3 sec
        pyautogui.press('enter')
    i=i+1