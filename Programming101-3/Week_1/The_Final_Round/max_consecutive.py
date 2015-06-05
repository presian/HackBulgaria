from group import group


def max_consecutive(items):
    return max([len(x) for x in [x for x in group(items)]])


def main():
    print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))


if __name__ == '__main__':
    main()
