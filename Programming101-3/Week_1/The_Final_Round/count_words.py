def count_words(arr):
    return {x: arr.count(x) for x in arr}


def main():
    print(count_words(["apple", "banana", "apple", "pie"]))
    print(count_words(["python", "python", "python", "ruby"]))


if __name__ == '__main__':
    main()
