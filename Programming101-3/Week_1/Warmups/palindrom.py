def palindrome(obj):
    return str(obj) == str(obj)[::-1]


def main():
    print (palindrome(121))
    print (palindrome("kapak"))
    print (palindrome("baba"))

if __name__ == '__main__':
    main()
