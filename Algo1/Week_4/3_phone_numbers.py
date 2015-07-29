def find_all_components(graph):
    counter = 0
    graph_len = len(graph)
    visited = [None] * graph_len
    for i in range(graph_len):
        if visited[i] is None:
            DFS(graph, i, visited)
            counter += 1
    return counter


def DFS(graph, start_point, visited):
    if visited[start_point] is None:
        visited[start_point] = True
        for e in graph[start_point]:
            if visited[e] is None:
                return DFS(graph, e, visited)


def main():
    students_count = int(input())
    students_numbers = [int(x) for x in input().split()]
    graph = []
    for i in range(students_count):
        student_phone_book = input().split()
        current_student_friend_list = []
        for j in range(1, len(student_phone_book)):
            current_student_friend_list.append(students_numbers.index(int(student_phone_book[j])))
        graph.append(current_student_friend_list)

    print(find_all_components(graph))

if __name__ == '__main__':
    main()
