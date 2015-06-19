from binary_search import binary_search


def quadruplets(arr_one, arr_two, arr_three, arr_four):
    first_pairs_sums = []
    for e_one in arr_one:
        for e_two in arr_two:
            first_pairs_sums.append(e_one + e_two)

    second_pairs_sums = []
    for e_three in arr_three:
        for e_four in arr_four:
            second_pairs_sums.append(e_three + e_four)

    second_pairs_sums = sorted(second_pairs_sums)
    counter = 0

    for s in first_pairs_sums:
        search_result = 0
        while 0 <= search_result < len(second_pairs_sums):
            search_result = binary_search(s * -1, second_pairs_sums, search_result, None, True)
            if search_result >= 0:
                counter += 1
                search_result += 1

    return counter


def main():
    print(quadruplets([5, 3, 4], [-2, -1, 6], [-1, -2, 4], [-1, -2, 7]))

if __name__ == '__main__':
    main()
