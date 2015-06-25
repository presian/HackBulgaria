from node import Node


class BST:

    def __init__(self):
        self.__root = None
        self.__size = 0

    def insert(self, key, value=None, current_node=None):
        if current_node is None:
            current_node = self.__root
        if self.__size == 0:
            self.__root = Node(key, value)
            self.__size = 1
        else:
            new_node = Node(key, value)
            while True:
                if current_node.get_key() <= new_node.get_key():
                    if self.__check_child_for_add(current_node, 'r'):
                        current_node.add_rigth_child(new_node)
                        new_node.add_parent(current_node)
                        break
                    else:
                        current_node = current_node.get_right_child()
                else:
                    if self.__check_child_for_add(current_node, 'l'):
                        current_node.add_left_child(new_node)
                        new_node.add_parent(current_node)
                        break
                    else:
                        current_node = current_node.get_left_child()
            self.__size += 1

    def lookup(self, value):
        current_node = self.__root
        while current_node is not None:
            if current_node.get_key() == value:
                return current_node
            elif current_node.get_key() > value:
                current_node = current_node.get_left_child()
            else:
                current_node = current_node.get_right_child()

    def remove(self, key):
        node = self.lookup(key)
        parent_node = node.get_parent()
        if parent_node is None:
            if node.get_right_child() is not None:
                most_left_key = self.__pop_most_left_from_node(node)
                self.__root.add_key(most_left_key)
                self.__root.add_parent = None
            elif node.get_left_child() is not None:
                self.__root = node.get_left_child()
                self.__root.add_parent = None
            else:
                self.__root = None
        elif node.get_left_child() is None and node.get_right_child() is None:
            if parent_node.get_left_child().get_key() == node.get_key():
                parent_node.add_left_child(None)
            elif parent_node.get_right_child().get_key() == node.get_key():
                parent_node.add_rigth_child(None)
        elif node.get_right_child() is None:
            if parent_node.get_left_child().get_key() == node.get_key():
                parent_node.add_left_child(node.get_left_child())
            elif parent_node.get_right_child().get_key() == node.get_key():
                parent_node.add_rigth_child(node.get_left_child())
        else:
            new_nod_key = self.__pop_most_left_from_node(node)
            node.add_key(new_nod_key)

    def traverse(self, traverse_type=None):
        if traverse_type is None:
            print(self.__traverse(self.__root))
        else:
            return self.__traverse(self.__root, traverse_type)

    def __traverse(self, node, traverse_type=None):
        if traverse_type is None:
            if node is not None:
                keys = []
                left_result = self.__traverse(node.get_left_child())
                if left_result is not None:
                    keys += left_result
                keys.append(node.get_key())
                right_result = self.__traverse(node.get_right_child())
                if right_result is not None:
                    keys += right_result
                return keys
        else:
            if node is not None:
                nodes = []
                left_result = self.__traverse(node.get_left_child(), 1)
                if left_result is not None:
                    nodes += left_result
                nodes.append((node.get_key(), node.get_value()))
                right_result = self.__traverse(node.get_right_child(), 1)
                if right_result is not None:
                    nodes += right_result
                return nodes

    def is_valid(self):
        tree_like_list = self.__traverse(self.__root)
        for i in range(1, len(tree_like_list)):
            if tree_like_list[i] < tree_like_list[i - 1]:
                return False
        return True

    def __get_most_left_node_from_node(self, node):
        if node is not None:
            child = node.get_left_child()
            if child is not None:
                next_left = child.get_left_child()
                while next_left is not None:
                    child = next_left
                    next_left = next_left.get_left_child()
            return child
        return None

    def __pop_most_left_from_node(self, node):
        child = node.get_right_child()
        next_left = child.get_left_child()
        while next_left is not None:
            child = next_left
            next_left = child.get_left_child()
        result_key = child.get_key()
        up_child = child.get_right_child()
        child_parent = child.get_parent()
        if up_child is not None:
            child_parent.add_rigth_child(up_child)
            up_child.add_parent(child_parent)
        else:
            if child_parent.get_parent() is None:
                child_parent.add_rigth_child(None)
            else:
                child_parent.add_left_child(None)
        return result_key

    def __check_child_for_add(self, current_node, child_type):
        if child_type == 'r':
            if current_node.get_right_child() is None:
                return True
            return False
        else:
            if current_node.get_left_child() is None:
                return True
            return False

    def get_bst(self):
        return self.__root


def main():
    bst = BST()

    bst.insert('kak')
    bst.insert('aka')
    # bst.insert('w')
    # bst.insert('h')
    # bst.insert('b')
    # bst.insert('f')
    # bst.insert('a')
    # bst.insert(6)
    # bst.insert(2)
    # bst.insert(4)
    # bst.insert(3)
    # bst.insert(5)
    # bst.insert(11)
    # bst.insert(15)
    # bst.insert(18)
    # bst.traverse(1)
    print(bst.is_valid())

if __name__ == '__main__':
    main()
