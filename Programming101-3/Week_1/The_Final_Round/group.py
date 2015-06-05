def group(arr):
    result = []
    temp = []
    for x in range(0, len(arr) - 1):
        temp.append(arr[x])
        if arr[x + 1] != arr[x]:
            result.append(temp)
            temp = []
    if arr[len(arr) - 1] == arr[len(arr) - 2]:
        temp.append(arr[len(arr) - 1])
        result.append(temp)
    else:
        result.append(temp)
        temp = []
        temp.append(arr[len(arr) - 1])
        result.append(temp)
    return result


def main():
    print(group([1, 1, 1, 2, 3, 1, 1]))
    print(group([1, 2, 1, 2, 3, 3]))


if __name__ == '__main__':
    main()
