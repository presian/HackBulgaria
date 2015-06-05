def square(number):
    return number ** 2
# print(square(2))  # == 4
# print(square(5))  # == 25


def fact(number):
    result = 1
    for n in range(1, number + 1):
        result *= n
    return result
# print(fact(5))  # == 120
# print(fact(0))  # == 1
# print(fact(6))  # = 720


def membercount_elements(items):
    counter = 0
    for element in items:
        counter += 1
    return counter
# print(membercount_elements([]))  # == 0
# print(membercount_elements([1, 2, 3]))  # == 3


def member(x, xs):
    for item in xs:
        if item == x:
            return True
    return False
# print(member(1, [1, 2, 3]))
# True
# print(member("Python", ["Django", "Rails"]))
# False


def grades_that_pass(students, grades, limit):
    s = []
    for g in range(1, len(grades)):
        if grades[g] >= limit:
            s.append(students[g])
    return s

# students = ["Rado", "Ivo", "Maria", "Nina"]
# grades = [3, 4.5, 5.5, 6]

# result = grades_that_pass(students, grades, 4.0)
# print(result)
