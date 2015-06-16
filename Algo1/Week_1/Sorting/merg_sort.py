from random import randint


def merge_sort(arr):
    arr_len = len(arr)
    if arr_len % 2 == 0:
        arr_len -= 1

    pairs = []
    for i in range(0, arr_len, 2):
        pairs.append(arr[i:i + 2])

    for un_sorted_pair in pairs:
        if len(un_sorted_pair) == 2 and un_sorted_pair[0] > un_sorted_pair[1]:
            temp_var = un_sorted_pair[0]
            un_sorted_pair[0] = un_sorted_pair[1]
            un_sorted_pair[1] = temp_var

    temp_arr = []
    index = 1
    if len(pairs) == 1:
        return pairs[0]

    while len(pairs) < arr_len:
        pairs_len = len(pairs)
        if index < pairs_len:
            merged_pair = merge_elements(pairs[index], pairs[index - 1])
            temp_arr.append(merged_pair)
            if index == pairs_len - 2:
                temp_arr.append(pairs[index + 1])
            index += 2
        else:
            if len(temp_arr) == 1:
                pairs = temp_arr[0]
            else:
                pairs = temp_arr
            temp_arr = []
            index = 1
    return pairs


def merge_elements(arr_one, arr_two):
    len_one = len(arr_one)
    len_two = len(arr_two)
    left_index = 0
    right_index = 0

    merged_arr = []
    while len(merged_arr) < len_one + len_two:
        if arr_one[left_index] <= arr_two[right_index]:
            merged_arr.append(arr_one[left_index])
            left_index += 1
            if left_index == len_one:
                merged_arr = merged_arr + arr_two[right_index:]
        else:
            merged_arr.append(arr_two[right_index])
            right_index += 1
            if right_index == len_two:
                merged_arr = merged_arr + arr_one[left_index:]

    return merged_arr


def main():
    test_arr = [randint(0,  150) for x in range(0, randint(1, 2000))]
    print(test_arr)
    print(merge_sort(test_arr))


if __name__ == '__main__':
    main()
