import sys

def isUnique(str):
    chars = set()
    for char in str:
        if char in chars:
            return False
        chars.add(char)
    return True

def isUniqueNoDS(str):
    for i in range(0, len(str)-1):
        char = str[i]
        for j in range(i+1, len(str)):
            char2 = str[j]
            if char == char2:
                return False
    return True

if __name__ == "__main__":
    print(isUniqueNoDS(str(sys.argv[1])))
