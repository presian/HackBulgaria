from copy import deepcopy
from sum_matrix import sum_matrix


def if_les(num, decreaser):
    result = num - decreaser
    if result < 0:
        return 0
    return result


def bomb_loop(c, m):
    result = deepcopy(m)
    start_row_index = c[0] - 1
    end_row_index = c[0] + 1
    start_col_index = c[1] - 1
    end_col_index = c[1] + 1
    for i in range(start_row_index, end_row_index + 1):
        if i >= 0 and i < len(m[0]):
            for j in range(start_col_index, end_col_index + 1):
                if j >= 0 and j < len(m):
                    if c != (i, j):
                        result[i][j] = if_les(result[i][j], m[c[0]][c[1]])
    return result


def matrix_bombing_plan(m):
    row_len = len(m[0])
    col_len = len(m)
    result = {}
    for row in range(0, col_len):
        for col in range(0, row_len):
            result[(row, col)] = sum_matrix(bomb_loop((row, col), m))
    return result


def main():
    print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

if __name__ == '__main__':
    main()
