class Node:

    def __init__(self, key, left_child=None, right_child=None, parent=None):
        self.__key = key
        self.__left_child = left_child
        self.__right_child = right_child
        self.__parent = parent

    # def add_member(self, member, member_type):
    #     if member_type == 'k':
    #         self.__key = member
    #     elif member_type == 'l':
    #         self.__left_child = member
    #     elif member_type == 'r':
    #         self.__right_child = member
    #     elif member_type == 'p':
    #         self.__parent = member
    #     else:
    #         raise Exception('Invalid member type')

    # def get_member(self, member_type):
    #     if member_type == 'k':
    #         return self.__key
    #     elif member_type == 'l':
    #         return self.__left_child
    #     elif member_type == 'r':
    #         return self.__right_child
    #     elif member_type == 'p':
    #         return self.__parent
    #     else:
    #         raise Exception('Invalid member type')

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

    def __str__(self):
        return '[{} | key: {} | {}]'.format(self.__left_child, self.__key, self.__right_child)

    def __repr__(self):
        return self.__str__()
