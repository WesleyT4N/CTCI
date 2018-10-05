import sys

def oneChangeAway(str1, str2):
    if (abs(len(str2) - len(str1)) > 1):
        return False
    shorter = str1 if len(str1) < len(str2) else str2
    longer = str2 if len(str1) < len(str2) else str1
    i = 0
    j = 0
    foundDiff = False
    while (i < len(shorter) and j < len(longer)):
        if shorter[i] != longer[j]:
            if foundDiff:
                return False
            foundDiff = True
            if len(shorter) == len(longer):
                i += 1
        else:
            i += 1
        j += 1
    return True

if __name__ == '__main__':
    print(str(oneChangeAway(str(sys.argv[1]), str(sys.argv[2]))))