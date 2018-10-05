import sys

def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s3 = s1 + s1
    split = s3.find(s2)
    return split == 0 or s1[split:len(s1)] + s1[0:split] == s2

print(string_rotation('w', 'W'))