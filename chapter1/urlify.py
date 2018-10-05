import sys

def urlify(str):
    str = str.strip()
    while str.find(' ') != -1:
        loc = str.find(' ')
        str = str[0:loc] + '%20' + str[loc+1:]
    return str

def urlifyMutable(str, true_len):
    space_count = 0
    for i in range(0, len(str)):
        if str[i] == ' ':
            space_count += 1
    if (true_len < len(str)):
        str[true_len] = '\0'
    index = true_len + space_count * 2
    for i in range(true_len - 1, -1, -1):
        if str[i] == ' ':
            str[index - 1] = '0'
            str[index - 2] = '2'
            str[index - 3] = '%'
            index -= 3
        else:
            str[index - 1] = str[i]
            index -= 1
if __name__ == '__main__':
    s = str(sys.argv[1])
    print(urlify(s))
    urlifyMutable(s, len(s.strip()))
    print(s)