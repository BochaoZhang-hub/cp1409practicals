"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    print_class_details(data)

def print_class_details(data):
    for items in data:
        print(f"{items[0]} is taught by {items[1]} and has {items[2]} students.")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_datas = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        parts_list = list(parts)
        subject_datas.append(parts_list)
    input_file.close()
    return subject_datas

main()