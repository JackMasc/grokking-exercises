# Binary search is also a divide and conquer algorithm,
# write the base caase and the recursive case for binary search


def binary_search(my_list, number, start_index, end_index):
    middle_index = (end_index - start_index) // 2
    if my_list[middle_index] == number:
        return True
    if end_index-start_index == 1:
        return False
    if my_list[middle_index] > number:
        end_index = middle_index -1
    else:
        start_index = middle_index +1
    return binary_search(my_list, number, start_index, end_index)

def main():
    my_list = [0,2,4,5,7,10,11,12]
    result = binary_search(my_list, 6, 0, len(my_list))
    print(result)

if __name__ == "__main__":
    main()
    