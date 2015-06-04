from math import ceil


def revers_splitting(splitted_reversed_string):
    first_part = splitted_reversed_string[:(len(splitted_reversed_string) // 2)]
    second_part = splitted_reversed_string[(len(splitted_reversed_string) // 2):]
    return second_part + first_part


def extract_key(string):
    string_without_key_len = string[: string.rfind('~')]
    key_len = int(string[string.rfind('~') + 1:])
    key = string_without_key_len[key_len * -1:]
    rest = string_without_key_len[:key_len * -1]
    return (key, rest)


def extract_alphabet(string):
    tild_index = string.find('~')
    alpha_len = int(string[:tild_index])
    alphabet_start_index = tild_index + 1
    alphabet_end_index = tild_index + 1 + alpha_len
    alphabet = string[alphabet_start_index: alphabet_end_index]
    rest = string[alphabet_end_index:]
    return (alphabet, rest)


def make_index_list(alphabet, string):
    return [alphabet.find(a) for a in string]


def make_key_long(key, message_len):
    count = ceil(message_len / len(key))
    long_key = key * count
    return long_key[:message_len]


def get_message(start_list, long_key_index_list, alphabet):
    alpha_len = len(alphabet)
    result = []
    for i in range(0, len(start_list)):
        multiplier_one = start_list[i] + alpha_len - long_key_index_list[i]
        multiplier_zero = start_list[i] - long_key_index_list[i]
        if 0 <= multiplier_one < alpha_len:
            result.append(multiplier_one)
        else:
            result.append(multiplier_zero)

    return "".join([alphabet[x] for x in result])


def dispatcher(string):
    after_re_reverse = revers_splitting(string)
    extract_key_result = extract_key(after_re_reverse)
    key = extract_key_result[0]
    after_extracting_key = extract_key_result[1]
    extract_alphabet_result = extract_alphabet(after_extracting_key)
    alphabet = extract_alphabet_result[0]
    after_extrakting_alphabet = extract_alphabet_result[1]
    start_list = make_index_list(alphabet, after_extrakting_alphabet)
    encripted_key = make_key_long(key, len(after_extrakting_alphabet))
    long_key_index_list = make_index_list(alphabet, encripted_key)
    message = get_message(start_list, long_key_index_list, alphabet)
    return message


def main():
    print(dispatcher("vrItommseIal vihack~416~Ilocveakgrithms he"))
    print(dispatcher("rc hscesi tcrest~410~thisaecr .rcese"))
    print(dispatcher("fl k.ccfsIolskv.~312~ .Ifrckslovelvo"))
    print(dispatcher("o?uin uw?stutnfwat?~413~orwa? thfuisnnrsiu"))

if __name__ == '__main__':
    main()
