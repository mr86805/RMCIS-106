# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:11:04 2026

@author: apoll
"""
with open("M8P4TXT.txt", "w") as file:
    file.write("Widget,10,15\n")
    file.write("Hammer,2,10\n")
    file.write("Saw,4,8\n")


total_extended_price = 0
order_count = 0

print("Item\tQuantity\tPrice\tExtended Price")
print("-" * 50)

with open("M8P4TXT.txt", "r") as file:
    for line in file:
        item, quantity, price = line.strip().split(",")

        quantity = int(quantity)
        price = float(price)

        extended_price = quantity * price

        total_extended_price += extended_price
        order_count += 1

        print(f"{item}\t{quantity}\t\t{price:.2f}\t{extended_price:.2f}")

average_order = total_extended_price / order_count if order_count > 0 else 0


print("\nSummary:")
print(f"Total Extended Price: {total_extended_price:.2f}")
print(f"Number of Orders: {order_count}")
print(f"Average Order Value: {average_order:.2f}")