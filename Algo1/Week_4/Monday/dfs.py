from stack import Stack


class DFS:

    def __init__(self):
        self.__stack = Stack

    def traverse(self, graph, traverse_type=None):
        visited = []
        start_index = 0
        self.__stack.push(start_index)

        while self.stack.size() != 0:
            current = self.pop()
            if current is not None:
                pass


def main():
    dfs = DFS()
    dfs.traverse([
        [0, 1, 0, 1, 0, 2],
        [0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]])

if __name__ == '__main__':
    main()
