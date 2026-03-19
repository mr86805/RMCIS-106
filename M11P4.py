# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:38:17 2026

@author: apoll
"""

def compute_price(msrp, make, model, ev_code):

    if ev_code.upper() == 'Y':
        discount_percent = 0.10  
    else:
        discount_percent = 0.05

    discount_amount = msrp * discount_percent
    new_msrp = msrp - discount_amount


    tax = new_msrp * 0.07
    total_price = new_msrp + tax

    return total_price


def main():
    total_msrp_sum = 0
    total_sales_sum = 0

    while True:
        response = input("Do you want to enter a car? (Yes/No): ")

        if response.lower() == "no":
            break
        elif response.lower() == "yes":
            make = input("Enter make: ")
            model = input("Enter model: ")
            ev_code = input("Is it an electric vehicle? (Y/N): ")
            msrp_input = input("Enter MSRP: ")

            try:
                msrp = float(msrp_input)
            except ValueError:
                print("Invalid MSRP.\n")
                continue

            total_price = compute_price(msrp, make, model, ev_code)

        
            print(f"\nMake: {make}")
            print(f"Model: {model}")
            print(f"MSRP: ${msrp:.2f}")
            print(f"Out-the-door price: ${total_price:.2f}\n")

        
            total_msrp_sum += msrp
            total_sales_sum += total_price

        else:
            print("Please enter Yes or No.\n")


    print("\nSummary:")
    print(f"Total MSRP of all cars: ${total_msrp_sum:.2f}")
    print(f"Total Sales Price of all cars: ${total_sales_sum:.2f}")


main()