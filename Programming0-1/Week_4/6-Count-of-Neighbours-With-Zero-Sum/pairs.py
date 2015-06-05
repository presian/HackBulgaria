def count_zero_neighbours(numbers):
    length = len(numbers)
    counter = 0
    for n in range(0, length - 1):
        if numbers[n] + numbers[n + 1] == 0:
            counter += 1
    return counter

print(count_zero_neighbours([1, 2, -2, 0, 0, 5, -5, 3]))
