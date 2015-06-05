def is_string_palindrom(string):
    test_str = ''.join([l.lower() for l in string if l.isalpha()])
    return test_str == test_str[::-1]


def main():
    print(is_string_palindrom("Az obi4am ma4 i boza"))
    print(is_string_palindrom("A Toyota!"))
    print(is_string_palindrom("bozaaa"))
    print(is_string_palindrom(" kapak! "))


if __name__ == '__main__':
    main()
