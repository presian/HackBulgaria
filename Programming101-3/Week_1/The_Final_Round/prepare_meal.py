# This works
def powerable_of_number(n, num):
    counter = 0
    while n != 1:
        if n % num != 0:
            return (counter, n)
        n = n // num
        counter += 1
    return (counter, 1)


def meal_maker(spam_count, eggs_count):
    spam = ["spam"] * spam_count
    eggs = ["eggs"] * eggs_count
    if spam_count > 0 and eggs_count > 0:
        return " ".join(spam) + " and " + " ".join(eggs)
    return " ".join(spam) + " ".join(eggs)


def prepare_meal(num):
    power_of_three = powerable_of_number(num, 3)
    power_of_five = powerable_of_number(num, 5)
    if power_of_five[1] == 1 or power_of_three[1]:
        return meal_maker(power_of_three[0], power_of_five[0])
    return ""


def main():
    print(prepare_meal(5))
    print(prepare_meal(3))
    print(prepare_meal(27))
    print(prepare_meal(15))
    print(prepare_meal(45))
    print(prepare_meal(7))

if __name__ == '__main__':
    main()
