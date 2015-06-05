def to_number(arr):
    a = 1
    result = 0
    for digit in arr[::-1]:
        result += digit * a
        a = a * 10
    return result


def main():
    print(to_number([1, 2, 3]))
    print(to_number([9, 9, 9, 9, 9]))
    print(to_number([1, 2, 3, 0, 2, 3]))

if __name__ == '__main__':
    main()
