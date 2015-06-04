def is_palindorme(string):
    if string == string[::-1]:
        return True
    return False


def string_rotation(string):
    all_rotations = [(string[i:] if i == 0 else string[i:] + string[:i]) for i in range(0, len(string))]
    return all_rotations


def check_rotations(all_rotations):
    all_palindromes = [x for x in all_rotations if is_palindorme(x)]
    return all_palindromes


def print_result(array):
    if len(array) > 0:
        for element in array:
            print(element)
    else:
        print(None)


def main():

    all_rotations = string_rotation('labalaa')
    all_palindromes = check_rotations(all_rotations)
    print_result(all_palindromes)
    print('====================')

    all_rotations = string_rotation('akawwaka')
    all_palindromes = check_rotations(all_rotations)
    print_result(all_palindromes)
    print('====================')

    all_rotations = string_rotation('shakira')
    all_palindromes = check_rotations(all_rotations)
    print_result(all_palindromes)
    print('====================')

if __name__ == '__main__':
    main()
