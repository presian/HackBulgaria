from random import randint


def insert_sort(arr):
    arr_len = len(arr)
    for x in range(0, arr_len):
        if x < arr_len - 1 and arr[x] > arr[x + 1]:
            temp = arr[x+1]
            arr[x + 1] = arr[x]
            arr[x] = temp
        else:
            x = x + 1
    return arr


def main():
    test_arr = [randint(0,  100) for x in range(0, 10)]
    print(test_arr)
    print(insert_sort(test_arr))
if __name__ == '__main__':
    main()
