# Write a recursive function to find the maximum number in a list


def find_max(my_list):
    if len(my_list) == 1:
        return my_list[0]
    max_sublist = find_max(my_list[1:])
    if my_list[0] > max_sublist:
        return my_list[0]
    return max_sublist


def main():
    my_list = [1, 2, 35, 5, 3, 10, 3]
    max = find_max(my_list)
    print(max)


if __name__ == "__main__":
    main()
