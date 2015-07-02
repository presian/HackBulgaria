from stack import Stack


class DirectoriesValidator:

    # def __init__(self, graph):
    #     self.__grahp = graph

    def validate(self, graph, start_index=None):
        if start_index is None:
            start_index = 0
        stack = []
        visited = []
        current_track = []
        stack.append(start_index)
        current_track.append(start_index)

        while len(stack) != 0:
            current = stack[-1]
            stack = stack[:-1]
            if current is not None:
                for e in range(len(graph[current])):
                    if graph[current][e] == 1 and e not in visited:
                        stack.append(e)
            print(stack)
            visited.append(current)

        # while stack.size() != 0:
        #     current = stack.pop()
        #     if current is not None:
        #         counter = 0
        #         for i in range(len(graph[current])):
        #             if graph[current][i] == 1 and graph[current][i] not in visited:
        #                 stack.push(graph[current][i])
        #                 counter += 1
        #         visited.append(current)
        #         if counter == 0:
        #             pass
        #         else:
        #             current_track.append(current)


def main():
    graph = [[0, 1, 0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    # The real deal
    # graph = [[0, 1, 0, 0],
    #          [0, 0, 1, 1],
    #          [0, 0, 0, 0],
    #          [1, 0, 0, 0]]
    dv = DirectoriesValidator()
    dv.validate(graph)


if __name__ == '__main__':
    main()
