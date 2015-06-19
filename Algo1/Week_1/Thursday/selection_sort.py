import sys
from random import randint

def sel_sort(arr):
    arr_len = len(arr)
    sorted_arr = []
    visited = []

    last_min_index = 0
    for x in range(0, arr_len):
        min_el = sys.maxsize
        for i in range(0, arr_len):
            if x > 0:
                if sorted_arr[-1:][0] <= arr[i] < min_el and (i not in visited):
                    min_el = arr[i]
                    last_min_index = i  
            else:
                if arr[i] < min_el:
                    min_el = arr[i]
                    last_min_index = i
        visited.append(last_min_index)
        sorted_arr.append(min_el)
    return sorted_arr




def main():
    test_arr = [randint(0, 10) for x in range(0, 100)]
    print(test_arr)
    print(sel_sort(test_arr))

if __name__ == '__main__':
    main()