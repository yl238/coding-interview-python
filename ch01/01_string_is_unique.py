def is_unique_chars(string):
    if len(string) > 128:
        return False

    charset = {}
    for s in string:
        if s in charset:
            return False
        else:
            charset[s] = True
    return True


if __name__ == '__main__':
    s = 'abcdefe'
    print(is_unique_chars(s))