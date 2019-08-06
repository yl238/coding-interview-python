def replace_spaces(s1):
    return '%20'.join(s1.split())


if __name__ == '__main__':
    name = 'Mr. John Smith    '
    print(replace_spaces(name))