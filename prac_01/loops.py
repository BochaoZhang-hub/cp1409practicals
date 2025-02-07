for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a.
for o in range(0, 101, 10):
    print(o, end=' ')
print()

#b.
for p in range(20, 0, -1):
    print(p, end=' ')
print()

#c.
number_of_stars = int(input("input number of stars:(please give integers):"))
for q in range(0,number_of_stars,1):
    print("*", end='')
print()

#d.
number_of_stars = int(input("input number of stars:(please give integers):"))
"""
    get number
    for loop, i think i can use "i" for in range, print i * "*"
    Because default settings starts from 0 and pass by 1, 
    and there will be a blank row in the first row，
    so i have to eet it start from 1.
    Also the range is ended by the number - 1,
    so i need to add 1 to the number input.
"""
for a in range(1,number_of_stars+1):
    print(a*"*")
print()
