
from guitar import Guitar
"""estimated time : 30 mins 
actual time : 20 mins """
FILENAME = "guitars.csv"
def main():

    guitarscsv = load_guitarcsv()


    print_pricise_guitar_infor(guitarscsv)


def load_guitarcsv():
    guitarscsv = []
    with open(FILENAME,'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitarscsv.append(Guitar(name, year, cost))
    return guitarscsv


def print_pricise_guitar_infor(guitars):
    """This function prints the precise information of the guitar"""
    for i in range(len(guitars)):
        if guitars[i].is_vintage():
            vintage = "vintage"
        else:
            vintage = ""
        print(f"Guitar{i + 1}:{guitars[i].name:>30}({guitars[i].year}:>10),worth ${guitars[i].cost:>10} {vintage}")


main()