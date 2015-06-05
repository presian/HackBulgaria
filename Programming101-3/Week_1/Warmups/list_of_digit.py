def to_digit(n):
    return [int(x) for x in str(abs(n))]


def main():
    print(to_digit(123))
    print(to_digit(99999))
    print(to_digit(123023))

if __name__ == '__main__':
    main()
