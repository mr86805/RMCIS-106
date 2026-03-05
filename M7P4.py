# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:08:25 2026

@author: apoll
"""

response = input("Do you want to enter employee data? (Yes/No): ")

total_gross = 0     
count = 0           

while response.lower() == "yes" or response.lower() == "y":

    
    last_name = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate of pay: "))

    
    if hours > 40:
        gross_pay = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        gross_pay = hours * rate

   
    print("Employee:", last_name)
    print("Gross Pay:", gross_pay)

    
    total_gross += gross_pay
    count += 1

   
    response = input("Do you want to enter another employee? (Yes/No): ")


print("Total Gross Pay:", total_gross)
print("Number of Employees:", count)


if count > 0:
    average_pay = total_gross / count
    print("Average Pay:", average_pay)
else:
    print("No employee data entered.")