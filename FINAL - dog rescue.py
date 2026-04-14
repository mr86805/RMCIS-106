# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:48:53 2026

@author: apoll
"""

dogs = []

def display_menu():
    print("\nDog Rescue")
    print("1. Add Dogs")
    print("2. View Dogs")
    print("3. Find Dogs")
    print("4. Quit")

def addDog():
    name = input("Dog Name: ")
    breed = input("Dog Breed: ")
    age = input("Dog Age: ")
    weight = input("Dog Weight: ")

    dogs.append({
        "name": name,
        "breed": breed,
        "age": age,
        "weight": weight
    })

    print("Dog added!\n")

def viewDogs():
    print("\n--- Dog List ---")
    if not dogs:
        print("No dogs available\n")
    else:
        for d in dogs:
            print(d["name"] + " | " + d["breed"] + " | " + d["age"] + " | " + d["weight"])
    print()

def findDog():
    search = input("Enter dog name to search: ")

    for d in dogs:
        if d["name"].lower() == search.lower():
            print("\nFound Dog:")
            print(d["name"], d["breed"], d["age"], d["weight"])
            return

    print("Dog not found\n")

def menu():
    choice = ""

    while choice != "Quit":
        display_menu()
        choice = input("Enter choice: ")

        if choice == "Add Dogs":
            addDog()
        elif choice == "View Dogs":
            viewDogs()
        elif choice == "Find Dogs":
            findDog()
        elif choice == "Quit":
            print("bye")
        else:
            print("Invalid choice\n")

def main():
    menu()

main()