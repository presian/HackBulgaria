class Histogram():

    def __init__(self):
        self.__server_list = {}

    def add(self, server_name):
        if server_name in self.__server_list:
            self.__server_list[server_name] = self.__server_list[server_name] + 1
        else:
            self.__server_list[server_name] = 1

    def count(self, server_name):
        if server_name in self.__server_list:
            return self.__server_list[server_name]
        return None

    def get_dict(self):
        return self.__server_list
