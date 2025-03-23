from guitar import Guitar
"""estimated time : 30 mins 
actual time : 20 mins """

FILENAME = "guitars.csv"

def main():
    guitarscsv = load_guitarcsv()
    guitarscsv.sort()
    print_pricise_guitar_infor(guitarscsv)


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
