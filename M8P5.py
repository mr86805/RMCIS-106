# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:17:42 2026

@author: apoll
"""


file = open("M8P5TXT.txt", "w")
file.write("Jones,1,12\n")
file.write("Adams,1,10\n")
file.write("Baker,0,12\n")
file.write("Smith,0,16\n")
file.close()

total = 0
count = 0

print("Item\tQuantity\tPrice\tExtended Price")
print("-" * 50)


file = open("M8P5TXT.txt", "r")

for line in file:
    item, quantity, price = line.strip().split(",")

    quantity = int(quantity)
    price = float(price)

    extended_price = quantity * price

    total += extended_price
    count += 1

    print(item, "\t", quantity, "\t\t", format(price, ".2f"), "\t", format(extended_price, ".2f"))

file.close()


if count > 0:
    average = total / count
else:
    average = 0


print("\nTotal of all extended prices:", format(total, ".2f"))
print("Number of orders:", count)
print("Average order value:", format(average, ".2f"))
