def is_increasing(seq):
    length = len(seq)
    if length > 1:
        for i in range(1, length):
            if seq[i] <= seq[i - 1]:
                return False
    return True


def main():
    print(is_increasing([1, 2, 3, 4, 5]))
    print(is_increasing([1]))
    print(is_increasing([5, 6, -10]))
    print(is_increasing([1, 1, 1, 1]))

if __name__ == '__main__':
    main()
