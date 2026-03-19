# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:33:02 2026

@author: apoll
"""

def compute_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats


def main():
    player_count = 0

    while True:
        last_name = input("Enter player's last name (or type 'q' to quit): ")
        
        if last_name.lower() == 'q':
            break
        
        hits_input = input("Enter number of hits: ")
        at_bats_input = input("Enter number of at bats: ")
        
        try:
            hits = float(hits_input)
            at_bats = float(at_bats_input)
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
            continue
        
    
        avg = compute_batting_average(hits, at_bats)
        
        
        print(f"Player: {last_name}")
        print(f"Batting Average: {avg:.3f}\n")
        
        player_count += 1

    
    print(f"Total number of players entered: {player_count}")


main()