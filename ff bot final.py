from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
from pynput.keyboard import Key, Controller



while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(522, 214)[0] == 0:
        keyboard.press("a")
        keyboard.release("a")
    if pyautogui.pixel(629, 214)[0] == 0:
        keyboard.press("s")
        keyboard.release("s")
    if pyautogui.pixel(729, 214)[0] == 0:
        keyboard.press('w')
        keyboard.release("w")
    if pyautogui.pixel(836, 214)[0] == 0:
        keyboard.press('d')
        keyboard.release("d")
