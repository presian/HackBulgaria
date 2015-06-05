from sys import argv
from random import randrange


def generate_numbers(filename, num):
    nums = " ". join([str(randrange(1, 1000)) for x in range(0, num)])
    file = open(filename, 'w')
    file.write(nums)
    file.close()


def has_arguments(count):
    return len(argv[1:]) >= count


def main():
    if has_arguments(2):
        filename = argv[1]
        num = int(argv[2])
        generate_numbers(filename, num)

if __name__ == '__main__':
    main()
