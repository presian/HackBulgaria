from random import randint


def quick_sort(arr):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    pivot = select_pivot(0, arr_len - 1)
    pivot_element = arr[pivot]
    less = []
    greater = []
    for i in range(arr_len):
        if i != pivot:
            current_element = arr[i]
            if current_element <= pivot_element:
                less.append(current_element)
            else:
                greater.append(current_element)
    return quick_sort(less) + [pivot_element] + quick_sort(greater)


    return arr


def select_pivot(left, right):
    return left + (right - left) // 2


def main():
    test_arr = [randint(0, 100) for x in range(0, 100)]
    print(test_arr)
    print(quick_sort(test_arr))


if __name__ == '__main__':
    main()
