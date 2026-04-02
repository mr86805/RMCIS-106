# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:23:35 2026

@author: apoll
"""

def load_data(filename):
    names = []
    averages = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                names.append(parts[0])
                averages.append(float(parts[1]))
    return names, averages

def display_data(names, averages):
    for i in range(len(names)):
        print(names[i], averages[i])

def search_player(names, averages, target):
    for i in range(len(names)):
        if names[i].lower() == target.lower():
            print(names[i], averages[i])
            return
    print("Player not found")

def main():
    filename = "C:\\Users\\apoll\\OneDrive\\Desktop\\CIS\\Module 12\\M8P3TXT.txt" "players.txt"
    names, averages = load_data("C:\\Users\\apoll\\OneDrive\\Desktop\\CIS\\Module 12\\M8P3TXT.txt")
    display_data(names, averages)

    while True:
        last_name = input("Enter a last name to search (or 'quit' to stop): ")
        if last_name.lower() == 'quit':
            break
        search_player(names, averages, last_name)

if __name__ == "__main__":
    main()