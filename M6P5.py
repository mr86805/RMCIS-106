# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 17:21:59 2026

@author: apoll
"""

last_name = "Mendez"
salary = 70000
job_level = 7

if job_level >=10: 
    bonus_rate = .25
if job_level == range(5, 9):
    bonus_rate = .2
else: 
    bonus_rate =.1
    
bonus = salary * bonus_rate

print(last_name)
print(bonus)