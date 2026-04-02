# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:48:32 2026

@author: apoll
"""

def compute_student_averages(students):
    averages = []
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        averages.append([name, avg])
    return averages

def compute_class_averages(students):
    total1 = total2 = total3 = 0
    count = len(students)

    for grades in students.values():
        total1 += grades[0]
        total2 += grades[1]
        total3 += grades[2]

    return [total1 / count, total2 / count, total3 / count]

def main():
    students = {
        "Smith": [88, 90, 85],
        "Adams": [92, 87, 91],
        "Baker": [79, 83, 80],
        "Mendez": [85, 88, 84],
        "Jones": [90, 91, 89]
    }

    student_averages = compute_student_averages(students)
    class_averages = compute_class_averages(students)

    print("Student Name\tAverage")
    print("----------------------------")
    for item in student_averages:
        print(f"{item[0]}\t\t{item[1]:.2f}")

    print("----------------------------")
    print(f"Class Avg G1\t{class_averages[0]:.2f}")
    print(f"Class Avg G2\t{class_averages[1]:.2f}")
    print(f"Class Avg G3\t{class_averages[2]:.2f}")

if __name__ == "__main__":
    main()