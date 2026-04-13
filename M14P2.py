# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:08:06 2026

@author: apoll
"""

class Student:
    first_name = "Ricky"
    last_name = "Mendez"
    district_code = "I"
    enrolled_credits = 0 
    
    def calculate_tuition(self):
        if self.district_code =="I":
            tuition = 250 * self.enrolled_credits
            return tuition
        else: 
            tuition = 250 * self.enrolled_credits
            return tuition
        
    
student1 = Student()

student1.first_name = "Ricky"
student1.last_name = "Mendez"
student1.district_code = "I"
student1.enrolled_credits = 12

print(f'Name: {student1.first_name}')

print(f'Tuition cost: {student1.calculate_tuition()}')