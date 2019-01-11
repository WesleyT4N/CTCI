def binary_to_string(n):
    s = '.'
    l = len(str(n).split('.')[1])
    num = n
    while num > 0:
        if len(s) >= 32:
            return "ERROR"
        
        r = num * 2
        if r >= 1:
            s += "1"
            num = r - 1
        else:
            s += "0"
            num = r
        print(s)
    return s

print(binary_to_string(0.125 + .25))