import sys
from random import randint


def insert_sort(arr):
    arr_len = len(arr)
    sorted_arr = arr

    for i in range(1, arr_len):
        first = arr[i - 1]
        second = arr[i]
        if first > second:
            arr[i] = first
            arr[i-1] = second
        for x in range(i, -1, -1):
            ff = arr[x]
            ll = arr[x-1]
            if ff < ll:
                arr[x-1] = ff
                arr[x] = ll
    first = arr[arr_len-1]
    arr[arr_len-1] = arr[0]
    arr[0] = first  
    return arr


def main():
    test_arr = [randint(0,  50000) for x in range(0, 500)]
    print(insert_sort(test_arr))

if __name__ == '__main__':
    main()
