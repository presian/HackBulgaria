import math


class BIT:

    def __init__(self, input_list):
        self.__list = self.__make_bit(input_list)
        self.__list_len = len(self.__list)

    def __make_bit(self, input_list):
        input_list = self.__check_input_list_len(input_list)
        result_list = self.__make_pair_sum_of_list(input_list)
        return_list = []
        return_list = result_list + return_list
        while 1 < len(result_list):
            result_list = self.__make_pair_sum_of_list(result_list)
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

    def __make_pair_sum_of_list(self, input_list):
        list_len = len(input_list)
        result_list = []
        for i in range(0, list_len - 1, 2):
            result_list.append(input_list[i] + input_list[i+1])
        return result_list

    def __get_parent(self, index):
        return index // 2

    def update(self, index, new_value, update_type=None):
        update_index = self.__list_len // 2 + index
        old_value = self.__list[update_index]
        if update_type is None:
            self.__list[update_index] = new_value
        else:
            self.__list[update_index] = self.__list[update_index] + new_value
        parent_index = self.__get_parent(update_index)
        diff = self.__list[update_index] - old_value
        while parent_index > 0:
            self.__list[parent_index] = self.__list[parent_index] + diff
            parent_index = self.__get_parent(parent_index)

    def get_bit(self):
        return self.__list


def main():
    bit = BIT([1, 2, 3, 4])
    bit.update(3, 5)
    print(bit.get_bit())

if __name__ == '__main__':
    main()
