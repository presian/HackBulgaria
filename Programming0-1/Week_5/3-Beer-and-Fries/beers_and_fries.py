def max_score(beers, fries):
    b = sorted(beers, reverse=True)
    f = sorted(fries, reverse=True)
    score = 0
    for i in range(0, len(b)):
        score += b[i] * f[i]
    return score
print(max_score([10, 11], [1, 5]))
print(max_score([5], [5]))
print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))
