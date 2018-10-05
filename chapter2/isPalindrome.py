def reverse(l):
    # go to tail while flipping pointer
    curr = l
    prev = None
    while curr.next:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    curr.next = prev
    return curr

def isPalindrome(l):
    rev = reverse(l)
    p1 = l
    p2 = rev
    while p1 && p2:
        if p1.data != p2.data
            return false
        p1 = p1.next
        p2 = p2.next
    return true

def isPalindrome(l):
    stack = []
    curr = l
    while curr:
        stack.append(curr.data)
        curr = curr.next
    
    curr2 = l
    while curr2:
        if curr2.data != stack.pop():
            return False
        curr2 = curr2.next
    return True

def leng(l):
    c = 0
    while l:
        l = l.next
        c += 1

class Result:
    def __init__(self, result, node):
        self.result = result
        self.node = node

def is_palindrome_helper(l, leng)
    if l is None || leng <= 0
        return Result(True, None)
    if leng == 1:
        return Result(True, l.next)
    res = is_palindrome_helper(l.next, leng - 2);
    if (!res.result or res.node is None):
        return res;
    res.result = l.data == res.node.data
    res.node = res.node.next
    return res;

def is_palindrome_rec(l):
    p = is_palindrome_helper(l, leng(l))
    return p.result
