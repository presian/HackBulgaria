def fibonacci(n):
    result = []
    a = 1
    b = 1

    while len(result) < n:
        result.append(a)
        c = a + b
        a = b
        b = c
    return result


def main():
    print(fibonacci(10))


if __name__ == '__main__':
    main()
