from contains_digit import to_digit


def is_number_balanced(n):
    nums = to_digit(n)
    return sum([x for x in nums[:len(nums) // 2]]) == sum([x for x in nums[len(nums) // 2 + len(nums) % 2::]])


def main():
    print(is_number_balanced(9))
    print(is_number_balanced(11))
    print(is_number_balanced(13))
    print(is_number_balanced(121))
    print(is_number_balanced(4518))
    print(is_number_balanced(28471))
    print(is_number_balanced(1238033))


if __name__ == '__main__':
    main()
