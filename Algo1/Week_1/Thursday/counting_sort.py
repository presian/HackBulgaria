from random import randint


def counting_sort(arr):
    arr_len = len(arr)
    arr_max = max(arr)

    # make list full with zeros and length equal to max lement of first list plus one
    zero_arr = make_zero_arr(arr_max)

    # counting elements
    for element in arr:
        zero_arr[element] = zero_arr[element] + 1

    sorted_arr = make_sorted_arr(zero_arr)
    return sorted_arr

def make_sorted_arr(zero_arr):
    arr_len = len(zero_arr)
    sorted_arr = []
    for i in range(arr_len):
        if zero_arr[i] != 0:
            sorted_arr += [i]*zero_arr[i]
    return sorted_arr


def make_zero_arr(arr_max):
    return [0]*(arr_max + 1)

def main():
    test_arr = [randint(0, 1500) for x in range(0, 1000)]
    print(test_arr)
    print(counting_sort(test_arr))


if __name__ == '__main__':
    main()
