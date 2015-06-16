from random import randint


def insert_sort(arr):
    arr_len = len(arr)

    for i in range(1, arr_len):
        first = arr[i - 1]
        second = arr[i]
        if first > second:
            arr[i] = first
            arr[i - 1] = second
        else:
            continue
        for x in range(i, 0, -1):
            ff = arr[x]
            ll = arr[x - 1]
            if ff < ll:
                arr[x - 1] = ff
                arr[x] = ll
    return arr


def main():
    test_arr = [randint(0,  200) for x in range(0, 10)]
    print(test_arr, '\n')
    print(insert_sort(test_arr))

if __name__ == '__main__':
    main()
