from binary_search import binary_search


def quadruplets(arr_one, arr_two, arr_three, arr_four):
    arr_two = sorted(arr_two)
    arr_three = sorted(arr_three)
    arr_four = sorted(arr_four)
    for e in arr_one:
        q_sum = e
        for i in range(0, len(arr_two)):
            pass
