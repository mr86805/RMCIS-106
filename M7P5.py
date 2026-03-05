# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:15:29 2026

@author: apoll
"""

response = input("Do you want to enter order data? (Yes/No): ")

total_discounts = 0   # sum of all discount amounts

while response.lower() == "yes" or response.lower() == "y":

    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    extended_price = quantity * price

    if extended_price > 10000:
        discount_percent = 0.25
    else:
        discount_percent = 0.10

    discount_amount = extended_price * discount_percent
    total = extended_price - discount_amount

    print("Extended Price:", extended_price)
    print("Discount Amount:", discount_amount)
    print("Total:", total)

    total_discounts += discount_amount

    response = input("Do you want to enter another order? (Yes/No): ")

print("Sum of all discounts:", total_discounts)