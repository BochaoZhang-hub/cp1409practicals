

print("Sequences learning tool")
print("1. Show the even numbers from x to y")
print("2. Show the odd numbers from x to y")
print("3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)")
print("4. Exit the program")
choice = int(input("Enter your choice: "))
while choice != 4:
    if choice == 1:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        for i in range (x, y+1, 1):
            if i % 2 == 0:
                print(i,end=' ')
        print()
    elif choice == 2:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        for i in range (x, y+1, 1):
            if i % 2 != 0:
                print(i,end=' ')
        print()
    elif choice == 3:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        for i in range (x, y+1, 1):
            print(i^2,end=' ')
        print()
    else:
        print("Invalid choice")
    print("Sequences learning tool")
    print("1. Show the even numbers from x to y")
    print("2. Show the odd numbers from x to y")
    print("3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)")
    print("4. Exit the program")
    choice = int(input("Enter your choice: "))
print("Exiting the program")