def string_matrix(matrix_width, strings):
    result = ''
    for word in strings:
        if len(word) > matrix_width:
            word = word[:matrix_width]
        elif len(word) < matrix_width:
            word += 'X' * (matrix_width - len(word))
        result += '| ' + ' | '.join(word) + ' |\n'
    return result


def main():
    print(string_matrix(6, ["python", "gogo", "perl", "java", "haskell", "ruby0nRails"]))

if __name__ == '__main__':
    main()
