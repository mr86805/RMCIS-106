# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 15:46:46 2026

@author: apoll
"""
#a = appliance. appliance name is fridge 
a = "fridge"
#price of appliance = 1200 = b
b = 1200
if b > 1000:
    warrantee_cost = .1 * b
    if b <= 1000:
        warrantee_cost = .05 * b

print(a)
print(b)
print(warrantee_cost)
total = b + warrantee_cost
print(total)