def quicksort(my_list):
    if len(my_list) < 2:
        return my_list
    else:
        pivot = my_list[0]
        smaller_list = [i for i in my_list[1:] if i <= pivot]
        greater_list = [i for i in my_list[1:] if i > pivot]
    return quicksort(smaller_list) + [pivot] + quicksort(greater_list)

def main():
    my_list = [1,4,31,6,5,4,15,2]
    sorted_list = quicksort(my_list)
    print(sorted_list)

if __name__ == "__main__":
    main()