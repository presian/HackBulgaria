from binary_index_three import BIT

class BirthdaysRange:

    def __init__(self):
        self.__list = BIT([0]*365)

    def add(self, index, value):
        self.__list.update(index, value, 1)

    def remove(self, index, value):
        self.__list.update(index, value * -1, 1)

    def count(self, start_index, end_index):
        start_range = min([start_index, end_index])
        end_range = max([start_index, end_index])
        return self.__list.sum_from_to(start_range, end_range)

    def get_bit(self):
        return self.__list.get_bit()


def main():
    br = BirthdaysRange()
    # br.add(11, 1)
    # br.add(12, 1)
    br.add(5, 1)
    br.add(10, 1)
    br.add(6, 1)
    br.add(7, 1)
    br.add(3, 1)
    br.add(4, 1)
    br.add(5, 1)
    br.add(11, 1)
    br.add(21, 1)
    br.add(300, 1)
    br.add(15, 1)

    print(br.count(2, 10))

    print(br.count(10, 365))

    br.add(8, 3)
    print(br.count(7, 11))

    br.remove(8, 2)
    print(br.count(7, 11))

    br.add(18, 5)
    print(br.count(10, 20))

    br.add(5, 1)
    print(br.count(5, 25))

    # may be is 1 no 10
    br.remove(5, 3)
    print(br.count(1, 10))

if __name__ == '__main__':
    main()
