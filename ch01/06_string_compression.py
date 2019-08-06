def compress_string(string):
    counter = 1
    char_list = []
    for i, ch in enumerate(string):
        if i == 0:
            char_list.append(ch)
        else:
            if ch != string[i-1]:
                char_list.append(str(counter))
                char_list.append(ch)
                counter = 1
            else:
                counter += 1
        if i == len(string)-1:
            char_list.append(str(counter))
    if len(char_list) < len(string):
        return ''.join(char_list)
    return string


if __name__ == '__main__':

    test_string = 'aabccccv'
    test_string = 'abababaaav'
    test_string = 'abaaaaaa'
    print(compress_string(test_string))