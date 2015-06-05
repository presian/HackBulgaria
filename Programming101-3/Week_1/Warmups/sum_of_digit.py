from list_of_digit import to_digit


def sum_of_digit(n):
    return sum(to_digit(n))


def main():
    print(sum_of_digit(-10))


if __name__ == '__main__':
    main()
