from sys import argv
from cat import file_reader


def multiple_file_reader(*arguments):
    for arg in arguments:
        file_reader(arg)


def has_argumetns(count):
    return len(argv[1:]) >= count


def main():
    if has_argumetns(2):
        multiple_file_reader(argv[1], argv[2])

if __name__ == '__main__':
    main()
