from vector import Vector


class Queue:

    def __init__(self):
        self.__queue = Vector()

    # Adds value to the end of the Queue.
    # Complexity: O(1)
    def push(self, value):
        self.__queue.add(value)

    # Returns value from the front of the Queue and removes it.
    # Complexity: O(1)
    def pop(self):
        if self.__queue.size() > 0:
            first_elemet = self.__queue.get(0)
            temp_vector = Vector()
            for i in range(0, self.__queue.size()):
                if i > 0:
                    temp_vector.add(self.__queue.get(i))
            self.__queue = temp_vector
            return first_elemet
        else:
            return None

    # Returns value from the front of the Queue without removing it.
    # Complexity: O(1)
    def peak(self):
        if self.__queue.size != 0:
            return self.__queue.get(0)
        return None

    # Returns the number of elements in the Queue.
    # Complexity: O(1)
    def size(self):
        return self.__queue.size()

    def get(self, index):
        if index < self.__queue.size():
            return self.__queue.get(index)
        return None

    def remove(self, index):
        self.__queue.remove(index)

    def getQueue(self):
        return self.__queue.getVector()


def main():
    q = Queue()
    print(q.getQueue())
    q.push(5)
    q.push(6)
    q.push(7)
    # q.push(5)
    # q.push(6)
    # q.push(7)
    # q.push(5)
    # q.push(6)
    # q.push(7)
    # q.push(5)
    # q.push(6)
    # q.push(7)

    print(q.getQueue())
    print(q.pop())
    print(q.getQueue())

    print(q.peak())
    print(q.getQueue())

    print(q.get(1))

    print(q.getQueue())
    print(q.size())


if __name__ == '__main__':
    main()
