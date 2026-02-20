# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 16:46:04 2026

@author: apoll
"""

part_number = 99
quantity = 15

if part_number == 10 or 55:
    unit_cost = 1
if part_number == 99:
    unit_cost = 2
if part_number == 80 or 70:
    unit_cost = 3

total_cost = quantity * unit_cost

print(part_number)
print(unit_cost)
print(total_cost)