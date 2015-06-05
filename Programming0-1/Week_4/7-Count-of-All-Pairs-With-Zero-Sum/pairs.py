def count_zero_pairs(numbers):
    length = len(numbers)
    counter = 0
    for i in range(0, length):
        for j in range(i, length):
            if numbers[i] + numbers[j] == 0:
                counter += 1
    return counter
print(count_zero_pairs([0, 2, -2, 5, 10]))
