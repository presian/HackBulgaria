from nan_expand import nan_expand


def iterations_of_nan_expand(expanded):
    if "NaN" in expanded or expanded == "":
        index = 0
        while True:
            current_expand = nan_expand(index)
            if current_expand == expanded:
                return index
            if len(current_expand) > len(expanded):
                return False
            index += 1
    return False


def main():
    print(iterations_of_nan_expand(""))
    print(iterations_of_nan_expand("Not a NaN"))
    print(iterations_of_nan_expand(
        'Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
    print(iterations_of_nan_expand("Show these people!"))


if __name__ == '__main__':
    main()
