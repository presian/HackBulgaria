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

    def __get_left_child_index(self, parent_index):
        return parent_index*2

    def __get_right_child_index(self, parent_index):
        return parent_index*2

    def __is_right_child(self, index):
        return index % 2 == 1

    def __is_left_child(self, index):
        return index % 2 == 0

    def __make_work_index(self, index):
        return self.__list_len // 2 + index - 1

    def __make_out_index(self, index):
        return index + 1 - (self.__list_len // 2)

    def __min_from_index_to_index(self, start_index, end_index):

        start = self.__make_work_index(start_index)
        end = self.__make_work_index(end_index)
        if self.__list[start] <= self.__list[end]:
            min_index = start
            min_value = self.__list[start]
        else:
            min_index = end
            min_value = self.__list[end]

        current_left_index = self.__get_parent(start)
        current_right_index = self.__get_parent(end)

        if not self.__is_left_child(start):
            current_left_index = self.__get_parent(start + 1)
        if not self.__is_right_child(end):
            current_right_index = self.__get_parent(end - 1)
        traverse_min = min_index
        while current_left_index >= 1:
            if current_left_index == current_right_index:
                traverse_min = current_left_index
                break
            current_left_index = self.__get_parent(current_left_index)
            current_right_index = self.__get_parent(current_right_index)
        traverse_min_value = self.__list[traverse_min]
        if traverse_min_value < min_value:
            min_index = traverse_min
            min_value = traverse_min_value
            while True:
                left_child_index = self.__get_left_child_index(min_index)
                if left_child_index <= self.__list_len and self.__list[left_child_index] == min_value:
                    min_index = left_child_index
                    continue
                right_child_index = self.__get_right_child_index(min_index)
                if right_child_index <= self.__list_len and self.__list[right_child_index] == min_value:
                    min_index = right_child_index
                    continue
                return self.__make_out_index(min_index)
        return self.__make_out_index(min_index)

    def __return(self):
        pass

    def get_min_in_interval(self, start_index, end_index):
        return self.__min_from_index_to_index(start_index, end_index)

    def get_rmq(self):
        return self.__list


def main():
    rmq = RMQ([1, 11, 3, 4, 0, 6, 7, 8])
    print(rmq.get_rmq())
    print(rmq.get_min_in_interval(2, 5))

if __name__ == '__main__':
    main()
