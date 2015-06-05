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
        open_list.append(expression[:1])
        expression = expression[1:]
        for ch in expression:
            if len(open_list) == 0:
                return False
            if ch in CLOSE_BRACKETS:
                current_open = open_list.pop()
                if not is_pair(current_open, ch):
                    return False
            if ch in OPEN_BRACKETS:
                if len(open_list) > 0 and (OPEN_BRACKETS.find(open_list[-1]) - OPEN_BRACKETS.find(ch)) != -1:
                    return False
                open_list.append(ch)
        return True
    else:
        return False

def calculate_expression(expression):
    expression = expression[1:-1]
    index = 0
    result_expression = ''
    for ch in expression:
        if ch in OPEN_BRACKETS:
            result_expression += ' + 2*'
            if expression[index + 1] not in CLOSE_BRACKETS:
                result_expression += '('
            else:
                result_expression += '0'
        elif ch in CLOSE_BRACKETS\
                and index != len(expression) - 1\
                and expression[index + 1] not in CLOSE_BRACKETS:
            if expression[index -1] not in OPEN_BRACKETS:
                result_expression += ')'
            result_expression += ' + '
        else:
            result_expression += ch
        index += 1
    return eval(result_expression)


def controller(expression):
    check_result = check_expression(expression)
    if check_result:
        print(calculate_expression(expression))
    else:
        print('NO')


def main():
    """
        valid expressions
    """
    controller('(123)') #123
    controller('[(123)(123)]') # 492
    controller('[23(123)12(123)]') # 527
    controller('{123[123(123)123(123)]23[123]2}') #1870
    controller('[123]') # 123
    controller('{123}') # 123

    """
        invalid expressions
    """
    controller('123(123)') #NO
    controller('(123[123])') #NO
    controller('[123(123])') #NO
    controller('[123{123}]') #NO
    controller('(123)(123)') #NO

    """
        Examples
    """
    controller('[123(145)38(37)812]') # 1337
    controller('{125[2][(1)][3]125}') # 264
    controller('[125()125()125()125]') # 500
    controller('{125()125}') # NO
    controller('{125[12]{125}[12]125}') #NO
    controller('{125[12(123]125}') #NO


if __name__ == '__main__':
    main()
