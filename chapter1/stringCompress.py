import sys

def string_compress(s):
    if s is None or len(s) <= 1:
        return s
    orig_len = len(s)
    new = ''
    last = ''
    count = 1
    for i in range(len(s)):
        if s[i] == last:
            count += 1
        else:
            if i != 0:
                new += (last + str(count))
                print(new)
            count = 1
        last = s[i]
    new += (last + str(count))
    if orig_len > len(new):
        return new
    return s

if __name__ == "__main__":
    print(string_compress(str(sys.argv[1])))

