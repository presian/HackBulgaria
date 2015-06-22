from node import Node


class BST:

    def __init__(self):
        self.__root = None
        self.__size = 0

    def isert(self, value, current_node=None):
        if current_node is None:
            current_node = self.__root
        if self.__size == 0:
            self.__root = Node(value)
            self.__size = 1
        else:
            while True:
                if current_node.get_key() < value:
                    if self.__check_child(value, current_node, 'r'):
                        break
                    else:
                        current_node = current_node.get_right_child()
                else:
                    if self.__check_child(value, current_node, 'l'):
                        break
                    else:
                        current_node = current_node.get_left_child()

    def __check_child(self, value, current_node, child_type):
        if child_type == 'r':
            if current_node.get_right_child() is None:
                current_node.add_rigth_child(value)
                return True
            return False
        else:
            if current_node.get_left_child() is None:
                current_node.add_left_child(value)
                return True
            return False

    def get_bst(self):
        return self.__root

def main():
    bst = BST()

    bst.isert(9)
    bst.isert(6)
    print(bst.get_bst())


if __name__ == '__main__':
    main()
