def find_dependencies(graph):
    graph_len = len(graph)
    visited = [None] * graph_len
    path = []
    for i in range(graph_len):
        if visited[i] is None:
            DFS(graph, i, visited, path)


def DFS(graph, start_point, visited, path):
    if visited[start_point] is None:
        visited[start_point] = True
        for i in graph[start_point]:
            if visited[i] is None:
                if graph[i] == [] or is_all_visited(visited, graph[i]) is True:
                    path.append(i)
                else:
                    return DFS(graph, i, visited, path)


def is_all_visited(visited, arr):
    for e in arr:
        if visited[e] is True:
            return False
    return True


def main():
    projects_count = int(input())
    projects = input().split()
    searched_project = input()
    start_point = projects.index(searched_project)
    project_dependencies = []
    for i in range(projects_count):
        current_row = input().split()
        project_dependencies.append([projects.index(x) for x in current_row[1:]])
    visited = [None] * len(project_dependencies)
    DFS(project_dependencies, start_point, visited, [])

if __name__ == '__main__':
    main()
