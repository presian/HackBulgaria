from queue import Queue


class Stack:

    def __init__(self):
        self.__stack = Queue()

    # Adds value to the end of the Stack.
    # Complexity: O(1)
    # push(value)
    def push(self, value):
        self.__stack.push(value)

    # Returns value from the end of the Stack and removes it.
    # Complexity: O(1)
    # pop()
    def pop(self):
        last_index = self.__stack.size()
        last_element = self.__stack.get(last_index)
        self.__stack.remove(last_index)
        return last_element

    # Returns value from the front of the Queue without removing it.
    # Complexity: O(1)
    def peek(self):
        return

    # Returns the number of elements in the Queue.
    # Complexity: O(1)
    def size():
        pass

    def getStack(self):
        return self.__stack.getQueue()


def main():
    stack = Stack()
    stack.push(3)
    stack.push(4)
    stack.push(1)
    stack.push(9)
    stack.push(3)
    stack.push(7)
    print(stack.getStack())

    stack.pop()
    print(stack.getStack())

if __name__ == '__main__':
    main()
