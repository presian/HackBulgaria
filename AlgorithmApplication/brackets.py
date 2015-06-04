OPEN_BRACKETS = ['{', '[', '(']
CLOSE_BRACKETS = ['}', ']', ')']


def check_start_end_brackets(expression):
    if expression[:1] not in OPEN_BRACKETS:
        return False
    if expression[-1:] not in CLOSE_BRACKETS:
        return False
    return True


def check_curly_brackets_is_outer(expression):
    if expression[1:].find(OPEN_BRACKETS[0]) != -1:
        return False
    if expression[:-1].find(CLOSE_BRACKETS[0]) != -1:
        return False
    return True


def chck_normal_brackets(expression):
    open_bracket = expression.find(OPEN_BRACKETS[2])
    close_bracket = expression.rfind(CLOSE_BRACKETS[2])
    if open_bracket = 0:
        if close_bracket == -1 or close_bracket < len():
            pass


def main():
    print(check_curly_brackets_is_outer('{asd}'))


if __name__ == '__main__':
    main()


# (123)
# \(\d+\)

# [(123)(123)]
#\[(\(\d+\))*\]

# {?(\d+)?\[?(\d+)?(\(\d+\))+?\]?(\d+)?}?
