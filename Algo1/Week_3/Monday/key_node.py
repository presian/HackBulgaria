class KeyNode:

    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def add_key(self, key):
        self.__key = key

    def get_key(self):
        return self.__key

    def add_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def __str__(self):
        return '[key: {} | value: {}]'.format(self.__key, self.__value)

    def __repr__(self):
        return self.__str__()
