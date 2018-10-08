#!/usr/bin/env python
"""
@program pySpammer.py
@author Mason McDaniel
@brief Quick program made to spam chat boxes I made to mess with friends on Discord
"""

# -*- coding: utf-8 -*-
from pynput.keyboard import Key, Controller
import time
import sys

def spammer(lines, spamLine, spamLines):
    x = 0
    z = 0
    keyboard = Controller()
    time.sleep(5)
    if lines == 1:
        keyboard.type(spamLine[0])
        keyboard.type("\n")
        sys.exit()
    while x < lines:
        if z == (spamLines - 1):
            keyboard.type(spamLine[z])
            keyboard.type("\n")
            z = 0
        else:
            z += 1
            keyboard.type(spamLine[z])
            keyboard.type("\n")
        x += 1

def fromFile():
    spamLines = 0
    spamLine = []
    x = 0
    f = open("spamLines.txt","r")
    f1 = f.readlines()[1:]
    for j in f1:
        spamLine.append(j)
    spamLines = len(spamLine)
    if spamLines < 1:
        print "File is empty please put spam in spamLines.txt"
        f.close()
        sys.exit()
    while x < spamLines:
        print spamLine[x]
        x += 1
    lines = input("Enter the number of lines to spam: ")
    if lines == 0:
        print "Please enter a number greater than 0"
    spammer(lines, spamLine, spamLines)
    f.close()

def fromInput():
    x = 0
    spamLine = []
    lines = input("Enter the number of lines to spam: ")
    if lines < 1:
        print "Please enter a number greater than 0\n"
        fromInput()
    spamLines = input("Enter number of unique spam lines: ")
    if spamLines < 1:
        print "Please enter a number greater than 0\n"
        fromInput()

    while x < spamLines:
        print "Enter unique spam line (", x ,"): "
        spamLine.append(raw_input())
        x += 1

    spammer(lines, spamLine, spamLines)

def main():
    choice = raw_input("Spam from file? (Y/N):  ")
    choice = choice.upper()
    if choice == 'Y':
        fromFile()
    elif choice == 'N':
        fromInput()
    else:
        print "Please enter Y or N"
        main()

if __name__ == "__main__":
    main()
