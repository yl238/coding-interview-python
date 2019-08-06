from collections import Counter


def are_permutations(s1, s2):
    if len(s1) != len(s2):
        return False

    if tuple(sorted(s1)) != tuple(sorted(s2)):
        return False

    return True


def are_permutations2(s1, s2):
    if len(s1) != len(s2):
        return False
    if Counter(s1) != Counter(s2):
        print(type(Counter(s1)))
        return False
    return True


if __name__ == '__main__':
    string1 = 'acdbe'
    string2 = 'eacbd'

    print(are_permutations2(string1, string2))
