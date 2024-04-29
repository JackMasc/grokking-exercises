import sys


def binary(number, mylist):
    iterations = 0
    min_index = 0
    max_index = len(mylist) - 1
    while max_index - min_index >= 1:
        iterations += 1
        half_index = (min_index + max_index) // 2
        if number > mylist[half_index]:
            min_index = half_index + 1
        elif number < mylist[half_index]:
            max_index = half_index - 1
        elif number == mylist[half_index]:
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
