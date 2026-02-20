# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 17:16:02 2026

@author: apoll
"""

#number of concert tickets
quantity = 200

if quantity >= 25:
    price_per_ticket = 50
if quantity == range(10, 24):
    price_per_ticket = 60
if quantity == range(5, 9):
    price_per_ticket == 70
if quantity < 5: 
    price_per_ticket = 75
    
total_cost = quantity * price_per_ticket
    
print(quantity)
print(price_per_ticket)
print(total_cost)