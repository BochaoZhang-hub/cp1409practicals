from guitar import Guitar
"""estimated time : 30 mins 
actual time : 20 mins """

FILENAME = "guitars.csv"

def main():
    guitarscsv = load_guitarcsv()
    guitarscsv.sort()
    print_pricise_guitar_infor(guitarscsv)

    added_guitars = add_new_guitars()
    if added_guitars:
        guitarscsv.extend(added_guitars)
        guitarscsv.sort()
        print_pricise_guitar_infor(guitarscsv)
    else:
        print("no guitars added")


    save_file(guitarscsv)


def save_file(guitarscsv):
    """This funciton will save the guitar back to csv file"""
    with open(FILENAME, 'w') as out_file:
        for guitar in guitarscsv:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def add_new_guitars():
    """This function will ask the users to input the guitars and add it into the list"""
    appeneded_guitars = []
    name = input("Type in your guitar's name: ")
    while name != "":
        year = int(input("year:"))
        price = float(input("whats the price? "))
        appeneded_guitars.append(Guitar(name, year, price))
        name = input("Type in your guitar's name")
    return appeneded_guitars

def load_guitarcsv():
    """This function will load the csv file and store it"""
    guitarscsv = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitarscsv.append(Guitar(name, year, cost))
    return guitarscsv


def print_pricise_guitar_infor(guitars):
    """This function prints the precise information of the guitars"""
    for i in range(len(guitars)):
        guitar = guitars[i]
        if guitar.is_vintage():
            vintage = " (vintage)"
        else:
            vintage = ""
        print(f"Guitar {i + 1}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage}")


main()
