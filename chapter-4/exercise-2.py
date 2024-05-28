# Write a recursive function to count the number of items in a list


def count(my_list):
    if my_list == []:
        return 0
    return 1 + count(my_list[1:])


def main():
    my_list = [2, 4, 5, 3, 5]
    length = count(my_list)
    print(length)


if __name__ == "__main__":
    main()
