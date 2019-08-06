import re


def is_palindrome(string):
    string = re.sub('[^A-Za-z]', '', string)
    unique_char_dict = {}
    for s in string.lower():
        if s in unique_char_dict:
            unique_char_dict[s] += 1
        else:
            unique_char_dict[s] = 1

    len_str_even = (len(string) % 2 == 0)

    n_odd = 0
    for _, val in unique_char_dict.items():
        if val % 2 != 0:
            n_odd += 1

    if len_str_even:
        if n_odd > 0:
            return False
    else:
        if n_odd != 1:
            return False
    return True


if __name__ == '__main__':
    test_string = 'Tact coa'
    print(test_string)
    print(is_palindrome(test_string))