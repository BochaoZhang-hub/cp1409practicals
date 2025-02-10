"""Module 2 - practical 2 """

def main():
    """This is the main function and it will check the password and print stars"""
    length_required = 10
    password = get_password(length_required)
    print_asterisks(password)


def get_password(length_required):
    """this function will get the password."""
    password = input("please enter your password: ")
    while len(password) < length_required:
        print("password is too short")
        password = get_password()
    return password


def print_asterisks(password):
    """This function will print asterisks of length length"""
    print(len(password) * "*")


    return password


main()