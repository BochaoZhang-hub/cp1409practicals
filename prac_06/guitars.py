from guitar_test import test_is_vintage
from guitar import Guitar
def main():
    guitars = []
    print("My guitars!")
    name = input("type in your guitars name:")
    year = int(input("type in the year of your guitar:"))
    cost = float(input("How much is the guitar?"))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} is added.\n")

    for i in range(len(guitars)):
        if test_is_vintage():
            print(f"Guitar{i+1}:{guitars[i][0]:>30}({guitars[i][1]}:>10),worth ${guitars[i][2]:>10} (vintage)")
        else :
            print(f"Guitar{i + 1}:{guitars[i][0]:>30}({guitars[i][1]}:>10),worth ${guitars[i][2]:>10}")

main()