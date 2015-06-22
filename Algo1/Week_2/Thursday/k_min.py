from heap_sort import HeapSort


class KList:

    def kth_minimum(self, numbers, k):
        if 0 < k <= len(numbers):
            sorter = HeapSort(numbers)
            sorted_numbers = sorter.h_sort()
            return self.__print_result(k, sorted_numbers[k - 1])
        else:
            return None

    def __print_result(self, k, value):
        ending = ''
        if k == 1:
            ending = 'st'
        elif k == 2:
            ending = 'nd'
        elif k == 3:
            ending = 'rd'
        else:
            ending = 'th'
        print('{}-{} smallest: {}'.format(k, ending, value))


def main():
    klist = KList()
    test_arr = [5, 2, 3, 6, 1, 4]
    klist.kth_minimum(test_arr, 1)
    klist.kth_minimum(test_arr, 3)
    klist.kth_minimum(test_arr, 6)

if __name__ == '__main__':
    main()
