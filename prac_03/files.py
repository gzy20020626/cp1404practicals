"""
get name
while name is not "":
    out_file.write(name)
    get name
close file

name = in_file.readline()
print name
close file


for number in NUMBERS:
    write number
close file


result = 0
first_two_numbers = in_file.readlines()[:2]
result = int(first_two_numbers[0]) + int(first_two_numbers[1])
print result
close file


target_file = NUMBERS_FILE
total = 0
open target_file for reading as in_file
for line in in_file.readlines():
    number = int(line)
    total += number
print total
close file
"""

NAME_FILE = "name.txt"
NUMBERS_FILE = "numbers.txt"
NUMBERS = [17, 42, 400]


out_file = open(NAME_FILE, 'w')
name = input("Entry your name(enter to exit): ")
while name is not "":
    out_file.write(f"{name}\n")
    name = input("Entry your name(enter to exit): ")
out_file.close()

in_file = open(NAME_FILE, 'r')
for name in in_file.readlines():
    name = name.strip()
    print(f"Your name is {name}")
in_file.close()


out_file = open(NUMBERS_FILE, 'w')
for number in NUMBERS:
    out_file.write(f"{number}\n")
out_file.close()

in_file = open(NUMBERS_FILE, 'r')
result = 0
first_two_numbers = in_file.readlines()[:2]
result = int(first_two_numbers[0]) + int(first_two_numbers[1])
print(f"result:{result}")
in_file.close()


target_file = NUMBERS_FILE
total = 0
in_file = open(target_file, 'r')
for line in in_file.readlines():
    number = int(line)
    total += number
print(f"total:{total}")
in_file.close()
