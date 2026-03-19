# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:41:34 2026

@author: apoll
"""

def compute_discount(quantity, price, discount_rate):
    total = quantity * price
    
    discount_amount = total * discount_rate
    discounted_price = total - discount_amount
    
    return discount_amount, discounted_price


def main():
    while True:
        qty_input = input("Enter quantity (or 'q' to quit): ")
        
        if qty_input.lower() == 'q':
            break
        
        price_input = input("Enter price: ")
        discount_input = input("Enter discount rate (e.g., 0.10 for 10%): ")
        
        try:
            quantity = float(qty_input)
            price = float(price_input)
            discount_rate = float(discount_input)
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
            continue
        
    
        discount_amount, discounted_price = compute_discount(
            quantity, price, discount_rate
        )
        
        
        print(f"\nQuantity: {quantity}")
        print(f"Price: ${price:.2f}")
        print(f"Discount Amount: ${discount_amount:.2f}")
        print(f"Discounted Price: ${discounted_price:.2f}\n")


main()