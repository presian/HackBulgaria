def binary_search(element, g_list, left=None, right=None, most_left_in_left_bound=False):
    if left is None:
        left = 0
    if right is None:
        right = len(g_list) - 1

    arr_len = len(g_list)
    if element < g_list[left]\
        or element > g_list[right]\
        or arr_len == 0\
            or arr_len == 1 and g_list[0] != element:
        return -1

    mid_point = make_mid_point(left, right)
    mid_point_value = g_list[mid_point]

    if element == mid_point_value:
        while mid_point > 0 and g_list[mid_point - 1] == element:
            if most_left_in_left_bound is True and mid_point == left:
                return mid_point
            mid_point -= 1
        return mid_point
    elif element < mid_point_value:
        return binary_search(element, g_list, left, mid_point - 1, most_left_in_left_bound)
    else:
        return binary_search(element, g_list, mid_point + 1, right, most_left_in_left_bound)


def make_mid_point(left, right):
    return left + (right - left) // 2


def quadruplets(arr_one, arr_two, arr_three, arr_four):
    first_pairs_sums = []
    for e_one in arr_one:
        for e_two in arr_two:
            first_pairs_sums.append(e_one + e_two)

    second_pairs_sums = []
    for e_three in arr_three:
        for e_four in arr_four:
            second_pairs_sums.append(e_three + e_four)

    second_pairs_sums = sorted(second_pairs_sums)
    counter = 0

    for s in first_pairs_sums:
        search_result = 0
        while 0 <= search_result < len(second_pairs_sums):
            search_result = binary_search(s * -1, second_pairs_sums, search_result, None, True)
            if search_result >= 0:
                counter += 1
                search_result += 1

    print(counter)


def main():
    list_length = input()
    input_lists = []
    for i in range(0, 4):
        input_as_str_arr = input().split()
        input_as_digit_arr = []
        for s in input_as_str_arr:
            input_as_digit_arr.append(int(s))
        input_lists.append(input_as_digit_arr)
    quadruplets(input_lists[0], input_lists[1], input_lists[2], input_lists[3])
    # quadruplets([5, 3, 4], [-2, -1, 6], [-1, -2, 4], [-1, -2, 7])

if __name__ == '__main__':
    main()
