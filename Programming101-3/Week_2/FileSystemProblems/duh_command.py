import os
from sys import argv


def get_folder_size(p):
    from functools import partial
    prepend = partial(os.path.join, p)
    return sum([(os.path.getsize(f) if os.path.isfile(f) else get_folder_size(f)) for f in map(prepend, os.listdir(p))])


def has_arguments(count):
    return len(argv[1:]) >= count


def main():
    if has_arguments(1):
        get_folder_size(argv[1])

if __name__ == '__main__':
    main()
