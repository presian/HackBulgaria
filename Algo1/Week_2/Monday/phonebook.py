def phonebook_searcher(phonebook, searched_elements):
    phonebook = sorted(phonebook, key=lambda x: x[0])
    result = []
    for element in searched_elements:
        search_result = binary_search(element, phonebook)
        if search_result != -1:
            result_name = phonebook[search_result][1]
        else:
            result_name = None
        result.append(result_name)
    print_query(result)


def print_query(query_result):
    for q in query_result:
        print(q)


def binary_search(element, g_list, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(g_list) - 1

    arr_len = len(g_list)
    if element < g_list[left][0]\
        or element > g_list[right][0]\
        or arr_len == 0\
            or arr_len == 1 and g_list[0] != element:
        return -1

    mid_point = make_mid_point(left, right)
    mid_point_value = g_list[mid_point][0]

    if element == mid_point_value:
        while mid_point > 0 and g_list[mid_point - 1][0] == element:
            mid_point -= 1
        return mid_point
    elif element < mid_point_value:
        return binary_search(element, g_list, left, mid_point - 1)
    else:
        return binary_search(element, g_list, mid_point + 1, right)


def make_mid_point(left, right):
    return left + (right - left) // 2


def main():
    input_array = input().split()
    line_count = int(input_array[0])
    query_count = int(input_array[1])

    phonebook = []
    for i in range(0, line_count):
        new_entry = input().split()
        phonebook.append((int(new_entry[0]), new_entry[1]))

    searched = []
    for q in range(0, query_count):
        searched.append(int(input()))

    # phonebook = [(1, "Stanislav"), (15, "Rado"), (6, "Ivan"), (8, "Ivan")]
    # searched = [15, 8]
    phonebook_searcher(phonebook, searched)

if __name__ == '__main__':
    main()
