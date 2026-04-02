# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:59:33 2026

@author: apoll
"""

last_name = ["Smith", "Bartfast", "Moe", "Larry", "Curly", "Shemp", "Joe", "Snoopy", "Woodstock", "Popeye"]


#print(last_name[2])

def display_name():
    for x in last_name:
        print(x)
        
def display_name_reverse():
    last_name.reverse()
    for x in last_name:
        print(x)
        
display_name()
display_name_reverse()
