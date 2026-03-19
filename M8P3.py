# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:39:04 2026

@author: apoll
"""

filename = "C:\\Users\\apoll\\OneDrive\\Desktop\\CIS\\Module 8\\M8P3TXT.txt"

i = 0
with open(filename, "rt") as file:
    for line in file:
        i = i + 1 #this is to get everyother line
        line = line.strip()
        if i == 2 :
            print(i)
            print(line)
        if (int(line) >= 75000):
            print (line)