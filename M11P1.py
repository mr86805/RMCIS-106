# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:30:54 2026

@author: apoll
"""

def compute_total(quantity, price):
    total = quantity * price
    
    if total > 10000:
        total *= 0.9  
    
    return total


def main():
    grand_total = 0

    while True:
    
        qty_input = input("Enter quantity (or type 'q' to quit): ")
        
        if qty_input.lower() == 'q':
            break
        
        price_input = input("Enter price: ")
        
        try:
            quantity = float(qty_input)
            price = float(price_input)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        
        total = compute_total(quantity, price)
        
    
        print(f"Quantity: {quantity}")
        print(f"Price: ${price:.2f}")
        print(f"Total (after discount if applicable): ${total:.2f}\n")
        
        
        grand_total += total


    print(f"Total Extended Price: ${grand_total:.2f}")


main()