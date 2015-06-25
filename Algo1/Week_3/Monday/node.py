class Node:

    def __init__(self, key, value=None, left_child=None, right_child=None, parent=None):
        self.__key = key
        self.__left_child = left_child
        self.__right_child = right_child
        self.__parent = parent
        self.__value = value

    def add_left_child(self, left_child):
        self.__left_child = left_child

    def get_left_child(self):
        return self.__left_child

    def add_rigth_child(self, right_child):
        self.__right_child = right_child

    def get_right_child(self):
        return self.__right_child

    def add_parent(self, parent_node):
        self.__parent = parent_node

    def get_parent(self):
        return self.__parent

    def add_key(self, key):
        self.__key = key

    def get_key(self):
        return self.__key

    def add_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def __str__(self):
        return '[{} | key: {} | {}]'.format(self.__left_child, self.__key, self.__right_child)

    def __repr__(self):
        return self.__str__()
