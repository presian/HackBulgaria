from panda_allready_exist_error import PandaAlreadyThere


class PandaSocialNetwork:

    def __init__(self):
        self.__user_list = {}

    def get_panda_list(self):
        return self.__user_list

    def add_panda(self, panda):
        if self.has_panda(panda) is False:
            self.__user_list[panda] = []
        else:
            raise PandaAlreadyThere

    def make_friends(self, panda_ivo, panda_rado):
        if not self.has_panda(panda_ivo):
            self.add_panda(panda_ivo)
        if not self.has_panda(panda_rado):
            self.add_panda(panda_rado)
        self.__user_list[panda_ivo].append(panda_rado)
        self.__user_list[panda_rado].append(panda_ivo)

    def are_friends(self, panda_ivo, panda_rado):
        if not self.has_panda(panda_ivo) or not self.has_panda(panda_rado):
            return False
        if panda_ivo not in self.__user_list[panda_rado]:
            return False
        return True

    def has_panda(self, panda):
        return panda in self.__user_list

    def connection_level(self, panda_rado, panda_ivo):
        if not self.has_panda(panda_rado) or not self.has_panda(panda_ivo):
            return -1
        visited = set()
        queue = []
        path_to = {}

        queue.append(panda_rado)
        path_to[panda_rado] = None
        found = False
        path_length = 0

        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == panda_ivo:
                found = True
                break

            for neighbour in self.__user_list[current_node]:
                if neighbour not in visited:
                    path_to[neighbour] = current_node
                    visited.add(neighbour)
                    queue.append(neighbour)

        if found:
            while path_to[panda_ivo] is not None:
                path_length += 1
                panda_ivo = path_to[panda_ivo]

        if path_length == 0:
            path_length = -1
        return path_length

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False
        return self.__user_list[panda]
