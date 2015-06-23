class Node:

    def __init__(self, key, left_child=None, right_child=None):
        self.__key = key
        self.__left_child = left_child
        self.__right_child = right_child

    def add_left_child(self, left_child):
        self.__left_child = left_child

    def get_left_child(self):
        return self.__left_child

    def add_rigth_child(self, right_child):
        self.__right_child = right_child

    def get_right_child(self):
        return self.__right_child

    def get_key(self):
        return self.__key

    def __str__(self):
        return '{} | key: {} | {}'.format(self.__left_child, self.__key, self.__right_child)

    def __repr__(self):
        return self.__str__()
