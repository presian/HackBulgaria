# ugly but in one row ;)


def sands_of_time(width):
    return [''.join(['*' if ((r <= width / 2 and (c >= r and c < width - r)) or (r >= width / 2 and (c <= r and c >= width - r - 1))) else '.' for c in range(0, width)]) for r in range(0, width)]


def main():
    timer = sands_of_time(7)
    for x in timer:
        print(x)

if __name__ == '__main__':
    main()
