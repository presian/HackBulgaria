# graph - dict(key panda, )
# need github check


def bfs(graph, start, end):
    visited = set()
    queue = []

    # path_to[x] = y
    # if we go to x throught y

    path_to = {}

    queue.append(start)
    visited.append(start)
    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node == end:
            return True

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
