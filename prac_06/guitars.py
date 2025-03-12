
from guitar import Guitar
"""estimated time : 30 mins 
actual time : 20 mins """
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

    print_pricise_guitar_infor(guitars)


def print_pricise_guitar_infor(guitars):
    """This function prints the precise information of the guitar"""
    for i in range(len(guitars)):
        if guitars[i].is_vintage():
            vintage = "vintage"
        else:
            vintage = ""
        print(f"Guitar{i + 1}:{guitars[i].name:>30}({guitars[i].year}:>10),worth ${guitars[i].cost:>10} {vintage}")


main()