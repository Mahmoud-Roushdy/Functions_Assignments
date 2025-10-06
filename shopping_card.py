"""
# Shopping Cart Calculator

## Problem
You're building a shopping cart calculator for an online store. The program needs to:

1. Calculate the subtotal of items
2. Apply discounts based on different rules
3. Calculate tax
4. Add shipping costs
5. Display a formatted receipt

## Requirements
Without functions, this would involve repeating calculations and formatting code. Your task is to create functions that:

1. Eliminate repetitive calculations
2. Make the main program logic clear and easy to follow
3. Handle the price calculations step by step

## Expected Behavior
The program should allow users to add items to their cart, then display a detailed receipt with:
- Item list with prices
- Subtotal
- Discount applied (if any)
- Tax amount
- Shipping cost
- Final total

## Sample Run
```
Shopping Cart Calculator
========================

Enter item name (or 'checkout' to finish): Laptop
Enter price: 899.99

Enter item name (or 'checkout' to finish): Mouse
Enter price: 25.50

Enter item name (or 'checkout' to finish): Keyboard
Enter price: 75.00

Enter item name (or 'checkout' to finish): checkout

RECEIPT
=======
Laptop                           $899.99
Mouse                            $25.50
Keyboard                         $75.00
                               --------
Subtotal:                      $1000.49
Discount (10% for $1000+):      -$100.05
Tax (8.5%):                      $76.54
Shipping:                        $9.99
                               --------
TOTAL:                          $986.97
```

## Hints
Think about functions for:
- Calculating subtotals
- Determining and applying discounts
- Calculating tax
- Calculating shipping
- Formatting currency
- Printing receipt sections
"""


def calcualte_bill(items):
    subtotal = 0
    discount = 0

    for item in items:
        subtotal += int(items[item])
    if subtotal == 500:
        discount = subtotal * 0.05
    if subtotal >= 1000:
        discount = subtotal * 0.10
    tax = (subtotal * 8.5) / 100
    shipping = 9.99
    total = subtotal - discount + shipping + tax
    return subtotal, discount, tax, shipping, total


def print_recipt(input):
    bill = calcualte_bill(input)
    print("RECEIPT\n=======")
    for item, price in input.items():
        print(f"{item}\t\t\t ${price}")

    print("                      --------")
    print(f"Subtotal:\t\t\t ${bill[0]}:")
    print(f"Discount:\t\t\t -${bill[1]}:")
    print(f"Tax(% 8.5):\t\t\t ${bill[2]}:")
    print(f"shipping:\t\t\t ${bill[3]}:")
    print("                      --------")
    print(f"Total:\t\t\t ${bill[4]}:")


items = {}


while True:
    user = input("enter item")
    if user == "":
        break
    price = input("enter price")
    items[user] = price
print_recipt(items)
bill = calcualte_bill(items)
print(bill)
