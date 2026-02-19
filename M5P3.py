# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 15:41:12 2026

@author: apoll
"""

#number of books 
a = 12
#cost per book
b = 4
#order total
c = a * b

if c > 50:
    shipping = 0
if c <= 50:
    shipping = 25
    
print(c)
print(shipping)