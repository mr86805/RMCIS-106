# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:22:40 2026

@author: apoll
"""

class Student:
    tuition_rates = {
        "I": 250,
        "G": 250,   
        "X": 800
    }

    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    def calculate_tuition(self):
        rate = Student.tuition_rates.get(self.district_code, 250)
        return rate * self.enrolled_credits


student_I = Student("Ricky", "Mendez", "I", 12)
student_G = Student("Jackson", "Fry", "G", 9)
student_X = Student("Isaac", "Gallup", "X", 6)

students = [student_I, student_G, student_X]

for s in students:
    print(f"Name: {s.first_name} {s.last_name}")
    print(f"District Code: {s.district_code}")
    print(f"Tuition cost: ${s.calculate_tuition():.2f}")
    print("-" * 30)