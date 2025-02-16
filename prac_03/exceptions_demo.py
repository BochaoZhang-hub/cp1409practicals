"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
is_denominator_0 = False

while not is_denominator_0:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("invalid denominator, cant divided by 0")
        else:
            is_denominator_0 = True
            fraction = numerator / denominator
            print(fraction)

    except ValueError:
        print("Numerator and denominator must be valid numbers!")
        """
        Value Error will occur when the input of the numerator and denominator is not a int
        """
print("Finished.")
