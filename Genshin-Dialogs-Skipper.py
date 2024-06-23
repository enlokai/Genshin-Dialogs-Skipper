from ahk import AHK
import keyboard
import multiprocessing
import os
import psutil
import time


def startSkipping(stopSignal):
    keyboard.wait('f')
    while not stopSignal.is_set():
        win.click()
        win.send('f')


def stopSkipping(stopSignal):
    keyboard.wait('x')
    stopSignal.set()


def killSkipper(stopSignal):
    keyboard.wait('`')
    os.system("taskkill -f -im AutoHotkey64.exe")
    os.system("taskkill -f -im python.exe")
    stopSignal.set()


def getGenshinPID():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'GenshinImpact.exe':
            return process.info['pid']
    return None


pid = getGenshinPID()
ahk = AHK(executable_path='C:/Program Files/AutoHotkey/v2/AutoHotkey.exe')
win = ahk.win_get(title='ahk_pid {}'.format(pid))


if __name__ == "__main__":
    stopSignal = multiprocessing.Event()
    kill_process = multiprocessing.Process(target=killSkipper, args=(stopSignal,))
    kill_process.start()

    os.system("cls")
    print("\n\t~ Script Active & Running! ~"
          "\n\tStart Dialogue Skipping: F"
          "\n\tStop Dialogue Skipping: X"
          "\n\tDisable Skipping: `")

    while True:
        stopSignal = multiprocessing.Event()
        loop_process = multiprocessing.Process(target=startSkipping, args=(stopSignal,))
        keyboard_process = multiprocessing.Process(target=stopSkipping, args=(stopSignal,))
        
        loop_process.start()
        keyboard_process.start()

        loop_process.join()
        keyboard_process.join()