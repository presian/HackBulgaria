def is_an_bn(word):
    if word == "":
        return True
    if 'a' not in word or 'b' not in word:
        return False
    return word.count('a') * 'a' + word.count('a') * 'b' == word


def main():
    print(is_an_bn('ab'))
    print(is_an_bn('rado'))
    print(is_an_bn('aaabb'))
    print(is_an_bn('aaabbb'))
    print(is_an_bn('aabbaabb'))
    print(is_an_bn('bbbaaa'))
    print(is_an_bn('aaaaabbbbb'))


if __name__ == '__main__':
    main()
