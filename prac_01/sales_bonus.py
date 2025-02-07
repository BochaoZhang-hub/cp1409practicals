"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))

"""
#TODO: if input < 1000, bonus = 10%
if sales < 1000 :
    bonus = 0.1 * sales
    print(f"Your bonus is ${bonus:.2f}")

else :
    bonus = 0.15 * sales
    print(f"Your bonus is ${bonus:.2f}")

#comments:
#this code represents only the situation that we enter the correct positive number
#if we input negative numbers, the users still get negative 10% bonus.
"""

#improvement avoiding inputting negative numbers
"""
while sales < 0:
   print("invalid ammount")
   sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = 0.1 * sales
    print(f"Your bonus is ${bonus:.2f}")
else:
    bonus = 0.15 * sales
    print(f"Your bonus is ${bonus:.2f}")
"""

#Now add a loop to this, so it repeatedly asks for the user's sales and prints the bonus until they enter a negative number.
minimum_ammount = 1000
small_bonus = 0.1
big_bonus = 0.15
bonus = 0
while sales >= 0:
    if sales < minimum_ammount:
        bonus = small_bonus
    else:
        bonus = big_bonus
    bonus = sales * bonus
    print(f"Your bonus is ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
print("invalid ammount of sales")

