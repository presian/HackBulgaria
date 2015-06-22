class KLists:

    def __init__(self):
        self.__lists = []

    def merge(self, *lists):
        lists = list(lists)
        self.__lists = lists
        final_arr_len = sum([len(l) for l in lists])
        sorted_arr = []
        while len(sorted_arr) < final_arr_len:
            current_min = self.__get_current_min()
            sorted_arr.append(current_min)
        return sorted_arr

    def __get_current_min(self):
        first_members = []

        for l in self.__lists:
            first_members.append(l[0])

        min_index = first_members.index(min(first_members))
        min_value = first_members[min_index]
        self.__lists[min_index].pop(0)

        if len(self.__lists[min_index]) < 1:
            self.__lists.pop(min_index)
        return min_value


def main():
    klists = KLists()
    print(klists.merge([3, 5, 7, 9], [2, 4, 6], [0, 1, 8, 10], [-1, 15, 33, 21]))


if __name__ == '__main__':
    main()
