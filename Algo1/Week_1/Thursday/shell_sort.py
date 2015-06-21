from random import randint


def shell_sort(arr):
    arr_len = len(arr)
    index = 0
    power = 1
    gap = make_gap(arr_len, power)
    while gap > 0:
        first = arr[index]
        second = arr[index + gap]
        if first > second:
            arr[index] = second
            arr[index + gap] = first
            first_pivot = index
            second_pivot = index + gap
            while first_pivot >= 1 and arr[first_pivot] < arr[first_pivot - 1]:
                temp_var = arr[first_pivot]
                arr[first_pivot] = arr[first_pivot - 1]
                arr[first_pivot - 1] = temp_var
                first_pivot -= 1

            while second_pivot >= 1 and arr[second_pivot] < arr[second_pivot - 1]:
                temp_var = arr[second_pivot]
                arr[second_pivot] = arr[second_pivot - 1]
                arr[second_pivot - 1] = temp_var
                second_pivot -= 1

        if index + gap * 2 < arr_len:
            index = index + gap
        else:
            index = 0
            power += 1
            gap = make_gap(arr_len, power)
    return arr


def make_gap(arr_len, power):
    return arr_len // 2 ** power


def main():
    test_arr = [randint(0, 100) for x in range(0, 1000)]
    print(test_arr)
    print(shell_sort(test_arr))


if __name__ == '__main__':
    main()
