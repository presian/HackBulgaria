from fibonacci import fibonacci
from list_to_number import to_number


def fib_number(n):
    fibs = fibonacci(n)
    return to_number(fibs)


def main():
    print(fib_number(3))
    print(fib_number(10))

if __name__ == '__main__':
    main()
