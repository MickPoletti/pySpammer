# -*- coding: utf-8 -*-
from pynput.keyboard import Key, Controller
import time

x = 1
keyboard = Controller()

time.sleep(5)
while x < 100:
    keyboard.type(":emile: Hey :emile: guys :emile: Emile :emile: here\n")
    x+=1
