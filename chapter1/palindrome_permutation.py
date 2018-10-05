import sys

def is_palindrome_permutation(str):
    chars = {}
    oddCount = 0
    for char in str:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    for (char, count) in chars.items():
        if count % 2 != 0:
            oddCount += 1
    return oddCount <= 1
    
if __name__ == '__main__':
    print(str(is_palindrome_permutation(str(sys.argv[1]))))