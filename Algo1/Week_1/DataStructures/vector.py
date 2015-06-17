class Vector():

    def __init__(self):
        self.__size = 5
        self.__list = [None] * self.__size
        self.__index = 0

    def check_vector_length(self):
        if self.__index == self.__size:
            self.__list = self.__list + [None] * self.__size
            self.__size = self.__size * 2

    def add(self, value):
        self.check_vector_length()
        self.__list[self.__index] = value
        self.__index += 1

    def insert(self, index, value):
        self.check_vector_length()

        new_list = [None] * self.__size
        length = self.__size

        for i in range(0, length):
            if i > index and length > i + 1:
                new_list[i + 1] = self.__list[i]
            elif i == index:
                new_list[i] = value
                new_list[i + 1] = self.__list[i]
                self.__index += 1
            elif i < index:
                new_list[i] = self.__list[i]
            elif length == i + 1:
                new_list[length - 1] = new_list[i]
        self.__list = new_list

    def get(self, index):
        return self.__list[index]

    def remove(self, index):
        length = self.__size
        new_list = [None] * length

        for i in range(0, length):
            if i < index:
                new_list[i] = self.__list[i]
            elif i > index:
                new_list[i - 1] = self.__list[i]
        self.__list = new_list
        self.__index -= 1

        if self.__index > 0:
            self.__index = self.__index - 1
            self.__list[self.__index] = None

    def size(self):
        return self.__index

    def capacity(self):
        return self.__size

    def getVector(self):
        return self.__list


def main():
    vector = Vector()

    vector.add('lala')
    vector.add('asd')
    vector.add('rtr')
    vector.add('rtr')
    vector.add('rtr')

    vector.insert(2, 'lalalalal')
    vector.insert(2, 'lalalalal')
    vector.insert(2, 'lalalalal')
    vector.insert(2, 'lalalalal')
    vector.insert(2, 'lalalalal')
    vector.insert(2, 'lalalalal')

    print(vector.getVector())

    print(vector.get(1))

    vector.remove(1)
    print(vector.getVector())

    vector.pop()
    print(vector.getVector())

    print(vector.size())

    print(vector.capacity())


if __name__ == '__main__':
    main()
