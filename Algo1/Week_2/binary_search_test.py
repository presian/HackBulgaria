from random import randint

def generate_new_list(length):
    genereted_list = []
    for i in range(0, length):
        genereted_list.append(randint(0, 10))
    return sorted(genereted_list)


def find_element(element, g_list):
    left = 0
    right = len(g_list) - 1

    if element < g_list[left] or element > g_list[right]:
        return -1

    index = -1
    i = 0
    while left <= right:
        i += 1
        mid_point = (left + right)//2
        print(mid_point)

        if element > g_list[mid_point]:
            left = mid_point
        elif element < g_list[mid_point]:
            right = mid_point
        elif g_list[mid_point] == element:
            index = mid_point
            # if left == mid_point:
            #     return index
            # elif right - left > 1:
            #     right = mid_point
            # else:
            #     left += 1
        elif left == mid_point:
            return index
    return index


def main():
    # g_list = generate_new_list(12)
    g_list = [0, 1, 1, 1, 2, 2, 5]
    print(g_list)

    index = find_element(2, g_list)
    print(index)




if __name__ == '__main__':
    main()
