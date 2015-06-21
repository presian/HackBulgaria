class Heap:

    def __init__(self, heap_type=None):  # make min_heap by default
        self.__type = heap_type
        self.__heap = [None]
        self.__size = len(self.__heap)

    def insert(self, value):
        self.__heap.append(value)
        self.__size = self.__size + 1
        current_index = self.__size - 1
        parent_index = self.__get_parent_index(current_index)
        while parent_index > 0 and self.__is_need_to_swap(parent_index, current_index):
            self.__swap(parent_index, current_index)
            current_index = parent_index
            parent_index = self.__get_parent_index(current_index)

    def delete(self):
        if self.__size > 1:
            self.__swap(1, self.__size - 1)
            return_element = self.__heap[-1]
            self.__heap = self.__heap[:-1]
            self.__size = self.__size - 1
            self.__check_new_root()
            return return_element

    def __check_new_root(self):
        current_index = 1
        child_index = self.__get_child_index(current_index)
        exact_child_index = self.__get_exact_child_index(child_index)
        is_need_to_swap = self.__is_need_to_swap(current_index, exact_child_index)
        while current_index < self.__size and is_need_to_swap:
            self.__swap(current_index, exact_child_index)
            current_index = exact_child_index
            child_index = self.__get_child_index(current_index)
            exact_child_index = self.__get_exact_child_index(child_index)
            is_need_to_swap = self.__is_need_to_swap(current_index, exact_child_index)

    def __get_exact_child_index(self, child_index):
        if self.__type is None:
            if child_index < self.__size - 1 and self.__heap[child_index] > self.__heap[child_index + 1]:
                return child_index + 1
        else:
            if child_index < self.__size - 1 and self.__heap[child_index] < self.__heap[child_index + 1]:
                return child_index + 1
        return child_index

    def __is_need_to_swap(self, parent_index, child_index):
        if child_index < self.__size:
            if self.__type is None:
                return self.__heap[parent_index] > self.__heap[child_index]
            else:
                return self.__heap[parent_index] < self.__heap[child_index]
        return False

    def __swap(self, parent_index, current_index):
        temp = self.__heap[parent_index]
        self.__heap[parent_index] = self.__heap[current_index]
        self.__heap[current_index] = temp

    def __get_parent_index(self, index):
        parent = index // 2
        return parent

    def __get_child_index(self, parent_index):
        return parent_index * 2

    def getHeap(self):
        return self.__heap

    def size(self):
        return self.__size


def main():
    heap = Heap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(2)
    heap.insert(9)
    heap.insert(8)
    heap.insert(1)
    heap.insert(13)
    heap.insert(9)
    heap.insert(121)
    heap.insert(13)
    heap.insert(96)
    heap.insert(58)
    heap.insert(45)

    print(heap.getHeap())
    heap.delete()
    print(heap.getHeap())


if __name__ == '__main__':
    main()
