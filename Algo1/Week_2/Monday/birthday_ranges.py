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


def birth_days_ranges(birth_days, ranges):
    birth_days = sorted(birth_days)
    result = []
    for b_range in ranges:
        counter = 0
        for i in range(b_range[0], b_range[1] + 1):
            min_index = binary_search(i, birth_days)
            if min_index != -1:
                while min_index < len(birth_days) and birth_days[min_index] <= b_range[1]:
                    counter += 1
                    min_index += 1
                break
        result.append(counter)
    print_result(result)


def print_result(result_list):
    for r in result_list:
        print(r)


def main():
    first_line_input_as_string_arr = input().split()
    second_line_input_as_string_arr = input().split()
    birth_days = [int(x) for x in second_line_input_as_string_arr]
    ranges = []
    for r in range(0, int(first_line_input_as_string_arr[1])):
        ranges_as_str_arr = input().split()
        ranges.append((int(ranges_as_str_arr[0]), int(ranges_as_str_arr[1])))

    birth_days_ranges(birth_days, ranges)

if __name__ == '__main__':
    main()
