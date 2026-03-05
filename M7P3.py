# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:47:48 2026

@author: apoll
"""


response = input("Do you want to enter student exam data? (Yes/No): ")

count = 0  


while response.lower() == "yes" or response.lower() == "y":
    last_name = input("Enter student's last name: ")
    exam1 = float(input("Enter first exam score: "))
    exam2 = float(input("Enter second exam score: "))

  
    average = (exam1 + exam2) / 2

   
    print("Last Name:", last_name)
    print("Average Exam Score:", average)

    
    count += 1

    
    response = input("Do you want to enter another student? (Yes/No): ")


print("Number of students entered:", count)