def sum_diagonal(matrix):
    diagonal_sum = 0
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if row == col:
                diagonal_sum += matrix[row][col]
    return diagonal_sum


def magic_square(matrix):
    return sum([sum(x) for x in matrix])\
        + sum([sum(col) for col in zip(*matrix)])\
        + sum_diagonal(matrix)\
        + sum_diagonal([x[::-1] for x in matrix[::-1]])\
        == sum(matrix[0]) * (len(matrix) * 2 + 2)


def main():
    print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
    print(
        magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
    print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))


if __name__ == '__main__':
    main()
