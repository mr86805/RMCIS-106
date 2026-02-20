# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 16:55:31 2026

@author: apoll
"""

#principle amount of CD
principle_amount = 30000

#year to maturity of CD
years = 10


if principle_amount > 100000 and years == 5:
    interest_rate =.06
elif principle_amount == range(50000, 100000) and years == 10:
    interest_rate = .05
elif principle_amount == range(50000, 100000) and years == 5:
        interest_rate = .04
else:
    interest_rate = .02

first_year_interest = principle_amount * interest_rate

print(principle_amount)
print(interest_rate)
print(first_year_interest)


