def zero_insert(n):
    str_n = str(n)
    result = ""
    loop_range = len(str_n)
    for i in range(0, loop_range - 1):
        current_digit = str_n[i]
        next_digit = str_n[i + 1]
        if current_digit == next_digit or (int(current_digit) + int(next_digit)) % 10 == 0:
            result += current_digit + '0'
        else:
            result += current_digit
    result += str_n[-1::]
    return int(result)


def main():
    print(zero_insert(116457))
    print(zero_insert(55555555))
    print(zero_insert(1))
    print(zero_insert(6446))


if __name__ == '__main__':
    main()
