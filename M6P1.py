# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 16:27:37 2026

@author: apoll
"""

quantity = 20000

if quantity > 10000:
    price = 10
    if quantity == range(5000, 10000):
        price = 20
if quantity < 5000:
    price = 30
    
extended_price = quantity * price
tax = extended_price * .07
total = extended_price + tax

print(extended_price)
print(tax)
print(total)
