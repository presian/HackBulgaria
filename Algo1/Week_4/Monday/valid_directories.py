class DirectoriesValidator:

    # def __init__(self, graph):
    #     self.__grahp = graph

    def validate(self, graph, start_index=None):
        if start_index is None:
            start_index = 0
        stack = []
        in_stack = [False] * (len(graph))
        visited = []
        stack.append(start_index)
        in_stack[start_index] = True

        while len(visited) <= len(graph):
            if len(stack) == 0:
                new_root = [x for x in range(len(graph)) if x not in visited][0]
                stack.append(new_root)
                in_stack[new_root] = True
            current = stack[-1]
            if sum(graph[current]) == 0:
                stack = stack[:-1]
                in_stack[current] = False
            elif in_stack[current] is True and current in visited:
                stack = stack[:-1]
                in_stack[current] = False
            else:
                for e in range(len(graph[current])):
                    if graph[current][e] != 0:
                        if in_stack[e] is True:
                            return False
                        stack.append(e)
                        in_stack[e] = True

            visited.append(current)
        return True


def main():
    graph = [
            [0, 0, 0, 1, 0, 0],
            [0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

    dv = DirectoriesValidator()
    print(dv.validate(graph))


if __name__ == '__main__':
    main()
