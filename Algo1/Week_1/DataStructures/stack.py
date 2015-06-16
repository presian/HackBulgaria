from queue import Queue


class Stack:

    def __init__(self):
        self.__stack = Queue()

    def push(self, value):
        self.__stack.push(value)

    def pop(self):
        self.__stack.size()

    def getStack(self):
        return self.__stack.getQueue()


def main():
    stack = Stack()
    print(stack.getStack())

    stack = Stack()
    print(stack.getStack())

if __name__ == '__main__':
    main()
