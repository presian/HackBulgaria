from random import randint


def bubble_sort(arr):
    arr_len = len(arr)
    index = 0
    positions_change_counter = 0
    is_sorted = False
    while not is_sorted:
        index += 1
        if index < arr_len and arr[index - 1] > arr[index]:
            temp_var = arr[index]
            arr[index] = arr[index - 1]
            arr[index - 1] = temp_var
            positions_change_counter += 1
        if index == arr_len - 1:
            if positions_change_counter == 0:
                is_sorted = True
            positions_change_counter = 0
            index = 0
    return arr


def main():
    test_arr = [randint(0,  100) for x in range(0, 21)]
    print(test_arr)
    print(bubble_sort(test_arr))

if __name__ == '__main__':
    main()
