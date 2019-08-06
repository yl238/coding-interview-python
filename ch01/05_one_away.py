def one_edit_replace(first, second):
    n_diff = 0
    for s1, s2 in zip(first, second):
        if s1 != s2:
            n_diff += 1
    if n_diff != 1:
        return False
    return True


def one_edit_insert(s1, s2):
    index1 = 0
    index2 = 0
    while (index2 < len(s2)) and (index1 < len(s1)):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def is_one_away(first, second):
    if first == second:
        return True
    if len(first) == len(second):
        return one_edit_replace(first, second)
    if len(first)+1 == len(second):
        return one_edit_insert(first, second)
    if len(second)+1 == len(first):
        return one_edit_insert(second, first)
    return False


if __name__ == '__main__':
    str1 = 'pale'
    str2 = 'ple'

    print(is_one_away(str1, str2))