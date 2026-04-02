# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:46:02 2026

@author: apoll
"""

def main():
    students = {
        "Smith": 88,
        "Adams": 92,
        "Baker": 79,
        "Mendez": 85,
        "Jones": 90
    }

    total = 0

    print("Student Name\tGrade")
    print("------------------------")

    for name, grade in students.items():
        print(f"{name}\t\t{grade}")
        total += grade

    average = total / len(students)
    print("------------------------")
    print(f"Class Average\t{average:.2f}")

if __name__ == "__main__":
    main()