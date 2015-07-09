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

    def get_peak(self):
        if self.__size > 0:
            return self.__heap[1]
        return None


class Median:

    def __init__(self):
        self.__min_heap = Heap(1)
        self.__max_heap = Heap()
        self.__median = None

    def insert(self, number):
        if self.__min_heap.size() == 1 and self.__max_heap.size() == 1:
            self.__min_heap.insert(number)
            self.__median = self.__min_heap.get_peak()
            return self.__median

        self.__make_insert(number)
        self.__check_balance()

        if self.__min_heap.size() > self.__max_heap.size():
            self.__median = self.__min_heap.get_peak()
        else:
            self.__median = self.__max_heap.get_peak()

        return self.__median

    def __check_balance(self):
        if self.__min_heap.size() - self.__max_heap.size() > 1:
            min_peak = self.__min_heap.delete()
            self.__max_heap.insert(min_peak)
        elif self.__max_heap.size() - self.__min_heap.size() > 1:
            max_peak = self.__max_heap.delete()
            self.__min_heap.insert(max_peak)

    def __make_insert(self, number):
        if number < self.__median:
            self.__min_heap.insert(number)
        else:
            self.__max_heap.insert(number)


def main():
    number_counts = int(input())
    median = Median()

    for i in input().split():
        print(median.insert(int(i)))

if __name__ == '__main__':
    main()
