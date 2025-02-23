def main():
    """this function will ask the user to input 5 numbers and give response based on the numbers they input
    """
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_id = input("please type in your user name: ")
    while user_id in usernames:
        print("Access granted")
        numbers_limit = 5
        numbers = store_numbers(numbers_limit)

        print(f"The first number is {numbers[0]}")
        print(f"The last number is {numbers[-1]}")
        print(f"The smallest number is {min(numbers)}")
        print(f"The largest number is {max(numbers)}")
        print(f"The average of the number is {sum(numbers) / len(numbers):.1f}")
        print(numbers)
    print("Access Denied")



def store_numbers(numbers_limit):
    """This function will ask the user to type in the number and store it as a list"""
    numbers = []
    for i in range(numbers_limit):
        input_number = int(input("please type in the number: "))
        numbers.append(input_number)
    return numbers


main()