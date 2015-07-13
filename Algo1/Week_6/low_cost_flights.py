def floyd_warshall(distance_matrix, queries):
    matrix_len = len(distance_matrix)

    for k in range(0, matrix_len):
        for i in range(0, matrix_len):
            for j in range(0, matrix_len):
                not_direct_value = distance_matrix[i][k] + distance_matrix[k][j]
                if distance_matrix[i][j] > not_direct_value:
                    distance_matrix[i][j] = not_direct_value

    for x in queries:
        print(distance_matrix[x[0]][x[1]] if distance_matrix[x[0]][x[1]] != 1000000 else 'NO WAY')


def main():
    matrix_row_count = int(input())
    matrix = []
    for i in range(matrix_row_count):
        matrix.append([(int(x) if x != '0' else 1000000) for x in input().split()])
        matrix[i][i] = 0
    queries_count = int(input())
    queries = []
    for i in range(queries_count):
        queries.append([int(x) for x in input().split()])
    floyd_warshall(matrix, queries)


if __name__ == '__main__':
    main()
