import sys
import random


def selection_sort(mylist):
    list_length = len(mylist)
    for j in range(list_length):
        min_index = j
        for i in range(j + 1, list_length):
            if mylist[i] < mylist[min_index]:
                min_index = i
        mylist[j], mylist[min_index] = mylist[min_index], mylist[j]
    return mylist


def convert_user_input(user_input):
    try:
        integer = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        sys.exit()
    return integer


def main():
    length = convert_user_input(input("Please enter your list length: "))
    my_list = random.sample(range(1, 50), length)
    print(f"The random list of length {length} is: {my_list}")
    my_list = selection_sort(my_list)
    print(f"The sorted list is: {my_list}")


if __name__ == "__main__":
    main()
