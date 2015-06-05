def char_histogram(string):
    return {letter: string.count(letter) for letter in string}


def main():
    print(char_histogram("Python!"))
    print(char_histogram("AAAAaaa!!!"))

if __name__ == '__main__':
    main()
