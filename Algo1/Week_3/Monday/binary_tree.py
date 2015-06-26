from node import Node


class BinaryThree:

    def __init__(self):
        self.__root = None

    def insert(self, value):
        if self.__root is None:
            self.__root = Node(value)
        else:
            self.
