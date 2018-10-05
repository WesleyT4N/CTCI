import sys

def checkPermutationSort(str1, str2):
    if len(str1) != len(str2):
        return False
    sorted1 = sorted(str1)
    sorted2 = sorted(str2)
    for i in range(0, len(sorted1)):
        if sorted1[i] != sorted2[i]:
            return False
    return True

def checkPermutationCount(str1, str2):
    count1 = {}
    count2 = {}
    for char in str1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    for char in count2:
        if char in count1:
            count1[char] -= 1
            if count1[char] < 0:
                return False
        else:
            return False
    return True

if __name__ == "__main__":
    print(checkPermutationCount(sys.argv[1], sys.argv[2]))
