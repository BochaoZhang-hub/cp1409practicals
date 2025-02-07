def main():
    length_required = 10
    password = get_password()
    if len(password) < length_required:
        print("password is too short")
        password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """This function will print asterisks of length length"""
    print(len(password) * "*")


def get_password():
    """This function will let the user enter a password"""
    password = input("please enter your password: ")
    return password


main()