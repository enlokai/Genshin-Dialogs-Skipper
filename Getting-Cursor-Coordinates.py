from ahk import AHK
import keyboard
import multiprocessing
import os
import psutil
import time

ahk = AHK(executable_path='C:/Program Files/AutoHotkey/v2/AutoHotkey.exe')

while True:
    os.system("cls")
    print(ahk.get_mouse_position(coord_mode='Screen'))
    time.sleep(1)