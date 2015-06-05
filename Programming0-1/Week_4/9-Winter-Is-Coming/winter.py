def winter_is_coming(seasons):
    if seasons[::-1].index('winter') >= 5:
        return True
    return False

print(winter_is_coming(
    ["winter", "summer", "summer", "summer", "spring", "srping"]))

print(winter_is_coming(
    ["winter", "summer", "summer", "spring", "srping"]))
