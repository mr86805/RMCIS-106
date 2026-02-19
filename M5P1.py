# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 15:23:56 2026

@author: apoll
"""

#quantity of item
a = 1200
if a >= 1000:
    price = 3
if a <= 1000:
    price = 5
    
unit_price = 20
extended_price = a * unit_price
tax = .07 * extended_price
total = extended_price + tax

print(a)
print(unit_price)
print(extended_price)
print(tax)
print(total)