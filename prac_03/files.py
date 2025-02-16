out_file = open("name.txt",'w')
name = input("type in your name: ")
print(f"{name}",file=out_file)
out_file.close()

in_file = open("name.txt",'r')
print(f"Hi, {in_file.readline().strip()}!")
in_file.close()

with open("numbers.txt",'r') as input_file:
    number1 = int(input_file.read(3).strip())
    number2 = int(input_file.read(3).strip())
    result = number1 + number2
    print(result)

with open("numbers.txt",'r') as input_file_2:
    for line in input_file_2:
        print(line)