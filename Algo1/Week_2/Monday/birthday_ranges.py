from binary_search import binary_search


def birth_days_ranges(birth_days, ranges):
    birth_days = sorted(birth_days)
    result = []
    for b_range in ranges:
        counter = 0
        for i in range(b_range[0], b_range[1] + 1):
            min_index = binary_search(i, birth_days)
            if min_index != -1:
                while min_index < len(birth_days) and birth_days[min_index] <= b_range[1]:
                    counter += 1
                    min_index += 1
                break
        result.append(counter)
    return result


def main():
    birth_days = [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15]
    ranges = [(4, 9), (6, 7), (200, 225), (300, 365)]
    print(birth_days_ranges(birth_days, ranges))

if __name__ == '__main__':
    main()
