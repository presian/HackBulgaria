def quadruplets(arr_one, arr_two, arr_three, arr_four):
    counter = 0
    for e_one in arr_one:
        for e_two in arr_two:
            for e_three in arr_three:
                for e_four in arr_four:
                    if e_one + e_two + e_three + e_four == 0:
                        counter += 1
    return counter

# vsi4ki ot purvite dva, i wseki ot vtorite dva i tyrsim kombinaciqta pyrviq + obratniq mu

def main():
    print(quadruplets([5, 3, 4], [-2, -1, 6], [-1, -2, 4], [-1, -2, 7]))

if __name__ == '__main__':
    main()
