"""
function shop_calculator()
    total = 0
    get number of items
    while num_items < 0
        display Invalid number of items!
        get number of items
    for each item
        get price of item
        total += price
    if total > 100
        total *= 0.9
   display items
"""

def shop_calculator():
    total = 0
    num_items = int(input("Number of items: "))
    while num_items < 0:
        print("Invalid number of items!")
        num_items = int(input("Number of items: "))
    for i in range(num_items):
        price = float(input("Price of item: "))
        total += price
    if total > 100:
        total *= 0.9
    print(f"Total price for {num_items} items is ${total:.2f}")


shop_calculator()