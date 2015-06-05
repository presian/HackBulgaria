def str_reverse(string):
    return string[::-1]

# print(str_reverse("Python"))
# print(str_reverse("kapak"))
# print(str_reverse(""))


def join(delimiter, items):
    return delimiter.join(items)

# print(join(" ", ["Radoslav", "Yordanov", "Georgiev"]))
# print(join("\n", ["line1", "line2"]))


def startswith(search, string):
    if search in string and string.index(search) == 0:
        return True
    return False

# print(startswith("Py", "Python"))
# print(startswith("py", "Python"))
# print(startswith("baba", "asdbaba"))


def endswith(search, string):
    if startswith(str_reverse(search), str_reverse(string)):
        return True
    return False

# print(endswith(".py", "hello.py"))
# print(endswith("kapak", "babakapak"))
# print(endswith(" ", "Python   "))
# print(endswith("py", "python"))


def trim(string):
    return string.strip()

# print(trim("   asda   "))
# print(trim(" spacious    "))
# print(trim("no here but yes at end   "))
# print(trim("                      "))
# print(trim("python"))
