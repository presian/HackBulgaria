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
