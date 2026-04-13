# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:59:01 2026

@author: apoll
"""
#my_list = 1
#object.method
#my_list.reverse()
#my_list = []
#grosspay = 0.0

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method that calculates bonus
    def calculate_bonus(self, bonus_rate):
        return self.salary * bonus_rate


emp1 = Employee("Ricky Mendez", 50000)

# Ask user for bonus rate
bonus_rate = float(input("Enter bonus rate (example 0.10 for 10%): "))

bonus = emp1.calculate_bonus(bonus_rate)

print(f"Employee: {emp1.name}")
print(f"Salary: ${emp1.salary:.2f}")
print(f"Bonus: ${bonus:.2f}")