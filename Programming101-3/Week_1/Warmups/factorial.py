def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    print(factorial(10))


if __name__ == '__main__':
    main()
