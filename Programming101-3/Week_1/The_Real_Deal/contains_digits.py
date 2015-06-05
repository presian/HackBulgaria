from contains_digit import to_digit


def contains_digits(number, digits):
    return sum([1 for x in to_digit(number) if x in digits]) == len(digits)


def main():
    print(contains_digits(402123, [0, 3, 4]))
    print(contains_digits(666, [6, 4]))
    print(contains_digits(123456789, [1, 2, 3, 0]))
    print(contains_digits(456, []))


if __name__ == '__main__':
    main()
