length_required = 10
password = input("please enter your password: ")
if len(password) < length_required:
    print("password is too short")
    password = input("please enter your password: ")
print(len(password)*"*")