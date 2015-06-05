def haed(sequence):
    return sequence[0]
# print(haed([1, 2, 3]))


def last(sequence):
    return sequence[-1]
# print(last([1, 2, 3]))


def tail(sequence):
    return sequence[1:]
# print(tail([1, 2, 3]))


def equal_lists(first_sequence, second_secuence):
    return first_sequence == second_secuence
# print(equal_lists([1, 2, 3], [1, 2, 3]))
# print(equal_lists([1, 1, 3], [1, 2, 3]))
# print(equal_lists([], []))


def count_item(element, sequence):
    return sequence.count(element)
# print(count_item(5, [1, 2, 3, 4, 5]))
# print(count_item("winter", ["winter", "winter"]))
# print(count_item(False, [True, True]))


def take(n, sequence):
    return sequence[:n]
# print(take(2, [1, 2, 3, 4, 5]))
# print(take(3, [3, 4, 5, 6, 7, 8]))
# print(take(10, [1]))


def drop(n, sequence):
    return sequence[n:]
# print(drop(1, [1, 2, 3]))
# print(drop(2, ["Python", "Ruby", "Django", "Rails"]))
# print(drop(10, [1]))
