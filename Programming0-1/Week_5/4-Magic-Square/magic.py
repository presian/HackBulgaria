def check_row_sum(square, first_row_sum):
    for r in square:
        if sum(r) != first_row_sum:
            return False
    return True


def check_column_sum(square, first_row_sum):
    for c in range(0, len(square[0])):
        column_sum = 0
        for r in range(0, len(square)):
            column_sum += square[c][r]
        if column_sum != first_row_sum:
            return False
    return True


def check_first_diagonal(square, first_row_sum):
    first_diagonal_sum = 0
    for i in range(0, len(square[0])):
        first_diagonal_sum += square[i][i]
    if first_diagonal_sum != first_row_sum:
        return False
    return True


def check_second_diagonal(square, first_row_sum):
    second_diagonal_sum = 0
    for i in range(0, len(square[0])):
        second_diagonal_sum += square[i][len(square[0]) - i - 1]
    if second_diagonal_sum != first_row_sum:
        return False
    return True


def magic_square(square):
    first_row_sum = sum(square[0])
    if not check_row_sum(square, first_row_sum):
        return False
    elif not check_column_sum(square, first_row_sum):
        return False
    elif not check_first_diagonal(square, first_row_sum):
        return False
    elif not check_second_diagonal(square, first_row_sum):
        return False
    return True


print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
