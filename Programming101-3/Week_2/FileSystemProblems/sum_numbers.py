from sys import argv


def sum_numbers(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    print(sum([int(x) for x in content.split(" ")]))


def has_arguments(count):
    return len(argv[1:]) >= count


def main():
    if has_arguments(1):
        sum_numbers(argv[1])

if __name__ == '__main__':
    main()
