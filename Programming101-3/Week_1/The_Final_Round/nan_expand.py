def nan_expand(times):
    result = ""
    if times == 0:
        return result
    for x in range(0, times):
        if x == 0:
            result += "Not a NaN"
        else:
            result = "Not a " + result
    return result


def main():
    print(nan_expand(0))
    print(nan_expand(1))
    print(nan_expand(2))
    print(nan_expand(3))


if __name__ == '__main__':
    main()
