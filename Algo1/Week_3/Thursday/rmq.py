class RMQ:

    def __init__(self, input_list):
        self.__list = self.__make_rmq(input_list)
        self.__list_len = len(self.__list)

    def __make_rmq(self, input_list):
        input_list = self.__check_input_list_len(input_list)
        result_list = self.__make_pair_min_of_list(input_list)
        return_list = []
        return_list = result_list + return_list
        while 1 < len(result_list):
            result_list = self.__make_pair_min_of_list(result_list)
            return_list = result_list + return_list
        return [None] + return_list + input_list

    # need for optimize this method
    def __check_input_list_len(self, input_list):
        list_len = len(input_list)
        power = 0
        temp = 2 ** power
        while temp < list_len:
            power += 1
            temp = 2 ** power

        diff = temp - list_len
        return input_list + [0] * diff

    def __make_pair_min_of_list(self, input_list):
        list_len = len(input_list)
        result_list = []
        for i in range(0, list_len - 1, 2):
            result_list.append(input_list[i] if input_list[i] <= input_list[i+1] else input_list[i+1])
        return result_list

    def __get_parent(self, index):
        return index // 2

    def __get_childs(self, parent_index):
        return parent_index*2

    def __is_right_child(self, index):
        return index % 2 == 1

    def __is_left_child(self, index):
        return index % 2 == 0

    def __make_work_index(self, index):
        return self.__list_len // 2 + index - 1

    def __min_from_index_to_index(self, start_index, end_index):

        current_start_index = self.__make_work_index(start_index)
        current_end_index = self.__make_work_index(end_index)
        if self.__list[current_start_index] <= self.__list[current_end_index]:
            min_index = current_start_index
            min_value = self.__list[current_start_index]
        else:
            min_index = current_start_index
            min_value = self.__list[current_end_index]

        start_parent = self.__get_parent(current_start_index)
        end_parent = self.__get_parent(current_end_index)

        if not self.__is_left_child(current_start_index):
            current_left_index == start_parent + 1
        if not self.__is_right_child(current_end_index):
            current_right_index == end_parent - 1

        while current_left_index >= 1:
            current_left_index = self.__get_parent(current_left_index)
            current_right_index = self.__get_parent(current_right_index)
            if current_left_index == current_right_index:
                traverse_min = current_left_index
                break
        # TODO: Add checking for min value
        return self.__list[min_index]

    def get_min_in_interval(self, start_index, end_index):
        return self.__min_from_index_to_index(start_index, end_index)

    def get_rmq(self):
        return self.__list


def main():
    bit = RMQ([1, 11, 3, 4, 5, 6, 7, 8])
    print(bit.get_rmq())
    print(bit.get_min_in_interval(2, 5))

if __name__ == '__main__':
    main()
