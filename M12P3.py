# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:05:49 2026

@author: apoll
"""

def load_data(filename):
    lastnames = []
    scores = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                lastnames.append(parts[0])
                scores.append(int(parts[1]))
    return lastnames, scores

def find_high_low(lastnames, scores):
    high_var = 0
    low_var = 999
    high_index = 0
    low_index = 0

    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print("Highest Score:", lastnames[high_index], high_var)
    print("Lowest Score:", lastnames[low_index], low_var)

def main():
    filename = "C:\\Users\\apoll\\OneDrive\\Desktop\\CIS\\Module 12\\M12P3TXT.txt"
    lastnames, scores = load_data(filename)
    find_high_low(lastnames, scores)

if __name__ == "__main__":
    main()