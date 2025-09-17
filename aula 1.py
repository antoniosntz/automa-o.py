import pyautogui as pa 
import time 

pa.pause=2
pa.press('win')
pa.write ('Microsoft Edge')
pa.press('enter')
time.sleep(3)
pa.write("youtube.com")
pa.press('Enter')