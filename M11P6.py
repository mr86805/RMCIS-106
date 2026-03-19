# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:43:35 2026

@author: apoll
"""

def compute_scores(score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3
    return total, average


def main():
    while True:
        last_name = input("Enter student's last name (or 'q' to quit): ")
        
        if last_name.lower() == 'q':
            break
        
        s1_input = input("Enter exam score 1: ")
        s2_input = input("Enter exam score 2: ")
        s3_input = input("Enter exam score 3: ")
        
        try:
            score1 = float(s1_input)
            score2 = float(s2_input)
            score3 = float(s3_input)
        except ValueError:
            print("Invalid input. Please enter numeric scores.\n")
            continue
        
        total, average = compute_scores(score1, score2, score3)
        
        print(f"\nStudent: {last_name}")
        print(f"Total Points: {total:.2f}")
        print(f"Average Score: {average:.2f}\n")


main()