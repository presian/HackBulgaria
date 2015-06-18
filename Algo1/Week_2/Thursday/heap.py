class Heap:

    def __init__(self, heap_type='max'):
        self.__type = heap_type
        self.__heap = [None]

    def insert(self, value):
        self.__heap.append(value)
        current_index = len(self.__heap) - 1
        parent_index = self.__get_parent_index(current_index)
        while parent_index > 0 and self.__check_parent(parent_index, current_index):
            self.__swap(parent_index, current_index)
            current_index = parent_index
            parent_index = self.__get_parent_index(current_index)

    def __check_parent(self, parent_index, current_index):
        is_parent_smaller = self.__heap[parent_index] < self.__heap[current_index]
        if parent_index == 0 or is_parent_smaller:
            return True
        else:
            return False

    def __swap(self, parent_index, current_index):
        temp = self.__heap[parent_index]
        self.__heap[parent_index] = self.__heap[current_index]
        self.__heap[current_index] = temp

    def __get_parent_index(self, index):
        parent = index // 2
        return parent

    def getHeap(self):
        return self.__heap


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


if __name__ == '__main__':
    main()
