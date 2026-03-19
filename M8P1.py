# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:16:16 2026

@author: apoll
"""

principal_amount = 0
interest_rate = 0
annual_interest = 0
total_interest = 0 
begin_balance = 0
end_balance = 0 

principal_amount = float(input("Enter principal amount: "))
begin_balance = principal_amount
interest_rate = float(input("Enter interest rate: "))

#loop
for i in range(5):
    annual_interest = begin_balance * interest_rate
    end_balance = begin_balance + annual_interest
    #dont need the next 2 "print" lines
    print("Year..........Begin Balance.........End Balance")
    print(i+1, "......", begin_balance, ".......", end_balance)
    begin_balance = end_balance
    total_interest = total_interest + annual_interest
    
    print("Annual interest: ", annual_interest)

print("Total interest: ", total_interest)