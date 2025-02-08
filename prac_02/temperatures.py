"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():

    MENU = """
    This is an temperature convert machine 
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            degree_celsius = float(input("Temperature in Celsius: "))
            temperature = convert_celsius_to_fahrenheit(degree_celsius)
            print(f"You converted temperature is {temperature:.2f} F")
        elif choice == "F":
            degree_fahrenheit = float(input("Temperature in Fahrenheit: "))
            temperature = convert_fahrenheit_to_celsius(degree_fahrenheit)
            print(f"You converted temperature is {temperature:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_celsius_to_fahrenheit(degree_celsius):
    #This function will help convert the input temperature from degree Celsius into degree Fahrenheit
    fahrenheit = degree_celsius * 9.0 / 5 + 32
    return fahrenheit

def convert_fahrenheit_to_celsius(degree_fahrenheit):
    #This function will help convert the input temperature from degree Celsius into degree Fahrenheit.
    celsius = 5 / 9 * (degree_fahrenheit - 32)
    return celsius

main()