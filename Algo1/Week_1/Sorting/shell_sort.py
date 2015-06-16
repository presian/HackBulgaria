from random import randint


def shell_sort(arr):
    arr_len = len(arr)
    is_sorted = False
    index = 0
    power = 1
    gap = make_gap(arr_len, power)
    while gap > 0:
        first = arr[index]
        second = arr[index + gap]
        if first > second:
            arr[index] = second
            arr[index + gap] = first
            pivot = index
            while pivot > 1 and arr[pivot] < arr[pivot - 1]:
                temp_var = arr[pivot]
                arr[pivot] = arr[pivot - 1]
                arr[pivot - 1] = temp_var
                pivot -= 1

        if index + gap * 2 < arr_len:
            index = index + gap
        else:
            if index == 0:
                return arr
            index = 0
            power += 1
            gap = make_gap(arr_len, power)
    return arr


def make_gap(arr_len, power):
    return arr_len // 2**power


def main():
    # test_arr = [randint(0, 10) for x in range(0, 100)]
    test_arr = [60, 84, 20, 35, 75, 73, 55, ]
    print(test_arr)
    print(shell_sort(test_arr))

if __name__ == '__main__':
    main()
