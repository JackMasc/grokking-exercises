import sys


def binary(number, mylist):
    iterations = 0
    while len(mylist) >= 1:
        iterations += 1
        half_number = (mylist[0] + mylist[-1]) / 2
        if number > half_number:
            mylist = [num for num in mylist if num > half_number]
        elif number < half_number:
            mylist = [num for num in mylist if num < half_number]
        elif number == half_number:
            return iterations
        else:
            return None


def convert_user_input(user_input):
    try:
        integer = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        sys.exit()
    return integer


def main():
    length = convert_user_input(input("Please enter your list length: "))
    number = convert_user_input(input("Please enter the integer to look for: "))
    mylist = list(range(length))
    response = binary(number, mylist)
    print("It took {} steps to find {} in your list.".format(response, number))


if __name__ == "__main__":
    main()
