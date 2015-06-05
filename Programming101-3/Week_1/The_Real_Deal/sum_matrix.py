def sum_matrix(matrix):
    return sum([sum(row) for row in matrix])


def main():
    print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))


if __name__ == '__main__':
    main()
