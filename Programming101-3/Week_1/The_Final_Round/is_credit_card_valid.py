def to_digit(n):
    return [int(x) for x in str(abs(n))]


def is_credit_card_valid(number):
    n = to_digit(number)[::-1]
    if len(n) % 2 == 0:
        return False
    return sum(to_digit(int("".join([str(n[x] * (sum([i for i in [1] if x % 2 == 1]) + 1)) for x in range(0, len(n))])))) % 10 == 0


def main():
    print (is_credit_card_valid(79927398713))
    print (is_credit_card_valid(79927398715))

if __name__ == '__main__':
    main()
