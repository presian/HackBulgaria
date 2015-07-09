class Node:

    def __init__(self, key, weight, vertex):
        self.__key = key
        self.__weight = weight
        self.__vertex = vertex

    def add_key(self, key):
        self.__key = key

    def get_key(self):
        return self.__key

    def add_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def add_vertex(self, vertex):
        self.__vertex = vertex

    def get_vertex(self):
        return self.__vertex

    def __str__(self):
        return '[key: {} | weight: {}]'.format(self.__key, self.__weight)

    def __repr__(self):
        return self.__str__()


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
            if child_index < self.__size - 1\
                    and self.__heap[child_index].get_key() > self.__heap[child_index + 1].get_key():
                return child_index + 1
        else:
            if child_index < self.__size - 1\
                    and self.__heap[child_index].get_key() < self.__heap[child_index + 1].get_key():
                return child_index + 1
        return child_index

    def __is_need_to_swap(self, parent_index, child_index):
        if child_index < self.__size:
            if self.__type is None:
                return self.__heap[parent_index].get_key() > self.__heap[child_index].get_key()
            else:
                return self.__heap[parent_index].get_key() < self.__heap[child_index].get_key()
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

    def get_peak(self):
        if self.__size > 0:
            return self.__heap[1]
        return None


class ShortCabelPath:

    def __init__(self, sportal):
        pass
