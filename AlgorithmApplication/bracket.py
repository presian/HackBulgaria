OPEN_BRACKETS = '{[('
CLOSE_BRACKETS = '}])'


def check_start_end_brackets(expression):
    if expression[:1] not in OPEN_BRACKETS:
        return False
    if expression[-1:] not in CLOSE_BRACKETS:
        return False
    if OPEN_BRACKETS.find(expression[:1]) != CLOSE_BRACKETS.find(expression[-1:]):
        return False
    return True

def is_pair(op, cl):
    open_index = OPEN_BRACKETS.find(op)
    close_index = CLOSE_BRACKETS.find(cl)
    return open_index == close_index

def check_expression(expression):
    if check_start_end_brackets(expression):
        open_list = []
        for ch in expression:
            # Extract this in another method
            if ch in CLOSE_BRACKETS:
                current_open = open_list.pop()
                if not is_pair(current_open, ch):
                    return False
            if ch in OPEN_BRACKETS:
                open_list.append(ch)
        return True
    else:
        return False

def main():
    expression = '(123)(123)'
    check_result = check_expression(expression)
    print(check_result)

if __name__ == '__main__':
    main()
