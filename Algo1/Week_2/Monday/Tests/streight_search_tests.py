def generate_new_list(length):
    genereted_list = []
    for i in range(1, length  + 1):
        genereted_list.append(i)
    return genereted_list


def find_element(element, g_list):
    for i in range(0, len(g_list)):
        if element == g_list[i]:
            return i
    return -1


def main():
    g_list = generate_new_list(100)
    index = find_element(100, g_list)
    print(index)


if __name__ == '__main__':
    main()
