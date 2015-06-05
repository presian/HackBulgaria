def calculate_coins(sum):
    coins = sorted([1, 2, 5, 10, 20, 50, 100], reverse=True)
    result = {
        1: 0,
        2: 0,
        5: 0,
        10: 0,
        20: 0,
        50: 0,
        100: 0
    }
    sum_value = int(sum * 100)
    for x in range(0, len(coins)):
        if sum_value == 0:
            return result
        temp_sum = sum_value // coins[x]
        if temp_sum > 0:
            result[coins[x]] = temp_sum
            sum_value = sum_value - temp_sum * coins[x]
        else:
            result[coins[x]] = 0
    return result
print(calculate_coins(8.94))
print(calculate_coins(0.53))
