def taken_name(surname_husband, surname_wife):
    return surname_husband in surname_wife


def main():
    print(taken_name('Petrov', 'Petrova'))
    print(taken_name("Ivanov", "Tsvetanova"))
    print(taken_name("Petrov", "Ivanova-Petrova"))

if __name__ == '__main__':
    main()
