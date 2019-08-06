def is_rotation(s1, s2):
    if len(s2) != len(s1):
        return False
    s1_concat = s1 + s1
    if s2 in s1_concat:
        return True
    return False

if __name__ == '__main__':
    x1 = 'waterbottle'
    print(is_rotation(x1, 'erbottlewa'))