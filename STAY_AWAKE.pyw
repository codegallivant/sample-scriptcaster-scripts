import pyautogui as pag
import time


def countdown(t, message):
	while t:
		mins, secs = divmod(t, 60)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		print(f"{message} {timeformat}", end = '\r')
		time.sleep(1)
		t = t-1
		
while True:
	pag.press('f15')
	countdown(60,"Forcing system to stay awake. Next F15 key press: ")			
