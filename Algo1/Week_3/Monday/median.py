from heap import Heap


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
    median = Median()
    print(median.insert(5))
    print(median.insert(6))
    print(median.insert(7))
    print(median.insert(4))
    print(median.insert(3))
    print(median.insert(10))
    print(median.insert(20))
    print(median.insert(30))
    print(median.insert(40))
    print(median.insert(50))

if __name__ == '__main__':
    main()
