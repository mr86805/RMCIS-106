# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:50:37 2026

@author: apoll
"""

def load_data(filename):
    players = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                players[parts[0]] = float(parts[1])
    return players

def display_players(players):
    print("Player Name\tAverage")
    print("----------------------------")
    for name, avg in players.items():
        print(f"{name}\t\t{avg:.3f}")

def main():
    filename = "C:\\Users\\apoll\\OneDrive\\Desktop\\CIS\\Module 12\\M8P3TXT.txt"
    players = load_data(filename)
    display_players(players)

if __name__ == "__main__":
    main()