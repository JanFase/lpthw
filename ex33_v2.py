from sys import argv

script, max_number , increment = argv
print("max_number=", max_number)

def create_numbers_list(max_number, increment):
    i = 0
    numbers = []

    while i < int(max_number) + 1:
        print(f"At the top i is {i}.")
        numbers.append(i)

        i += int(increment)
        print("Numbers now:  numbers")
        print(f"At the bottom i is {i}.")


    print("The numbers: ")
    for num in numbers:
        print(num)

create_numbers_list(max_number, increment)

