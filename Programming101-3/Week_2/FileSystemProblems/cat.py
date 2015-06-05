import sys


def file_reader(filename):
    file = open(filename, "r")
    content = file.read()
    print(content)
    file.close


def has_arguments(count):
    return len(sys.argv[1:]) >= count


def main():
    if has_arguments(1):
        file_reader(sys.argv[1])

if __name__ == '__main__':
    main()
