# Write out the code for the recursive sum function.


def sum(my_list):
    if my_list == []:
        return 0
    return my_list[0] + sum(my_list[1:])


def main():
    result = sum([1, 4, 5, 2])
    print(result)


if __name__ == "__main__":
    main()
