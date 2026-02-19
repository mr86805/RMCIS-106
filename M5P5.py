# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 16:00:55 2026

@author: apoll
"""

last_name = "Mendez"
dependents = 3
gross_income = 70,000

adjusted_gross_income = gross_income = (3 * 12000)
if adjusted_gross_income > 50000:
    tax_rate = .2
if adjusted_gross_income <= 50000:
    tax_rate = .1
    
income_tax_rate = adjusted_gross_income * tax_rate
if income_tax_rate > 0:
    income_tax = 100

    
print(last_name)
print(gross_income)
print(dependents)
print(adjusted_gross_income)
print(income_tax)