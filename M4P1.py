# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 19:17:01 2026

@author: apoll
"""

exam_one_total = 100 
exam_two_total = 100
exam_one_weighted_total = 0
exam_two_weighted_total = 0

exam_one_score = 0.0
exam_two_score = 0.0

total_score = 0.0

exam_one_weight = .6
exam_two_weight = .4

#ask user for exam scores
print("Enter exam one score:")
exam_one_score = float(input())
print("exam_one_score:", exam_one_score)

print("Enter exam two score:")
exam_two_score = float(input())
print("exam_two_score:", exam_two_score)

#calculate weighted grade
exam_one_weighted_total = exam_one_score * exam_one_weight
exam_two_weighted_total = exam_two_score * exam_two_weight

total_score = exam_one_weighted_total +exam_two_weighted_total

print("Total Score", total_score)

#print("Exam one:", exam_one_score)
