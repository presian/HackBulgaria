from list_of_digit import to_digit
from factorial import factorial


def fact_digits(n):
    return sum([factorial(d) for d in to_digit(n)])


def main():
    print(fact_digits(111))
    print(fact_digits(145))
    print(fact_digits(999))

if __name__ == '__main__':
    main()
