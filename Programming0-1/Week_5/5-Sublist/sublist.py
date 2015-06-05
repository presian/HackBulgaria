def sublist(list1, list2):
    for e in list1:
        if e not in list2:
            return False
    return True

print(sublist(["Python"], ["Python", "Django"]))
print(sublist(["Python", "Django"], ["Django", "Python"]))
print(sublist([1, 2], [1, 0, 1, 2, 2]))
print(sublist([], [1, 0, 1, 2, 2]))
