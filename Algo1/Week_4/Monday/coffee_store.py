from my_queue import Queue


class CoffeeFider:

    def __init__(self, matrix, shop_lists, start_index):
        self.__map = matrix
        self.__shop_lists = shop_lists
        self.__start_index = start_index

    def find_nearest_shop(self):
        visited = []
        queue = Queue()
        queue.push(self.__start_index)

        while queue.size() != 0:
            current = queue.pop()
            if current is not None:
                if self.__shop_lists[current] != 0:
                    return current
                for e in range(len(self.__map[current])):
                    if self.__map[current][e] != 0 and e not in visited:
                        queue.push(e)
            visited.append(current)
        return None


def main():
    cf = CoffeeFider(
        [[0, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0]],
        [0, 1, 0, 0, 1, 1],
        0)

    print(cf.find_nearest_shop())


if __name__ == '__main__':
    main()
