# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:36:33 2026

@author: apoll
"""

def compute_forecast(month, sales):
    forecast_percent = 0

    if month.lower() == "january":
        forecast_percent = 0.10
    elif month.lower() == "february":
        forecast_percent = 0.08
    elif month.lower() == "march":
        forecast_percent = 0.12
    elif month.lower() == "april":
        forecast_percent = 0.07
    elif month.lower() == "may":
        forecast_percent = 0.09
    elif month.lower() == "june":
        forecast_percent = 0.11
    elif month.lower() == "july":
        forecast_percent = 0.15
    elif month.lower() == "august":
        forecast_percent = 0.13
    elif month.lower() == "september":
        forecast_percent = 0.06
    elif month.lower() == "october":
        forecast_percent = 0.14
    elif month.lower() == "november":
        forecast_percent = 0.16
    elif month.lower() == "december":
        forecast_percent = 0.18
    else:
        forecast_percent = 0.05  


    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales


def main():
    while True:
        response = input("Do you want to enter sales data? (Yes/No): ")
        
        if response.lower() == "no":
            print("Program ended.")
            break
        
        elif response.lower() == "yes":
            last_name = input("Enter last name: ")
            month = input("Enter month: ")
            sales_input = input("Enter sales: ")
            
            try:
                sales = float(sales_input)
            except ValueError:
                print("Invalid sales amount.\n")
                continue
            
        
            forecast_sales = compute_forecast(month, sales)
            
        
            print(f"\nName: {last_name}")
            print(f"Month: {month}")
            print(f"Current Sales: ${sales:.2f}")
            print(f"Next Month Forecast: ${forecast_sales:.2f}\n")
        
        else:
            print("Please enter Yes or No.\n")


main()