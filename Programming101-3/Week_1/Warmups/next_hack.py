from palindrom import palindrome


def odd(n):
    return n % 2 != 0


def next_hack(n):
    while True:
        n = n + 1
        bin_str = '{0:0b}'.format(n)
        if palindrome(bin_str) and odd(bin_str.count('1')):
            print(bin_str.count('1'))
            return n


def main():
    print(next_hack(0))
    print(next_hack(10))
    print(next_hack(8031))


if __name__ == '__main__':
    main()
