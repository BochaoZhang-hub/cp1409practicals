"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message

"""

name = input("What is your name? ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input("What is your choice? ")
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input("What is your choice? ")
print("Finished")