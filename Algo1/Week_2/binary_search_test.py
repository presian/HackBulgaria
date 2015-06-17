from random import randint


def find_element(element, g_list, left=None, right=None):
    if left is None and right is None:
        left = 0
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
            mid_point -= 1
        return mid_point
    elif element < mid_point_value:
        return find_element(element, g_list, left, mid_point - 1)
    else:
        return find_element(element, g_list, mid_point + 1, right)


def make_mid_point(left, right):
    return left + (right - left) // 2


def main():
    g_list = sorted([randint(0, 5) for x in range(0, 10)])
    # g_list = [0, 1, 1, 2, 2, 2, 2, 3, 3, 5]
    print(g_list)

    index = find_element(2, g_list)
    print(index)


if __name__ == '__main__':
    main()
