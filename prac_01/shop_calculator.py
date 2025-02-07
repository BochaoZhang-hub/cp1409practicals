"""
    get no.of items
    init price of total = 0
    for in range(no.of items)
        input price
        price of total = price of total + price
    if price of total < 100 :
        print(price of total)
    else :
        price of total = 0.9 * price of total
        print(price of total)
"""

number_of_items = int(input("Please input the number of items: "))
total_price = 0
while number_of_items < 0:
    print("invalid numebr of items!")
    number_of_items = int(input("Please input the number of items: "))
for i in range(number_of_items):
    price = float(input("Please input the price of item: "))
    total_price += price
if total_price <= 100 :
    print(f"total price for {number_of_items} items is {total_price:.2f}")
else:
    total_price = total_price * 0.9
    print(f"total price for {number_of_items} items is {total_price:.2f}")