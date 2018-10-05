class Node:
    def __init(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def partition(head, x):
    curr = head
    left = None
    l_head = None
    right = None
    r_head = None
    while curr:
        if curr.data < x:
            if left:
                left.next = curr
            else:
                left = curr
                l_head = curr
            left = left.next
        else:
            if right:
                right.next = curr
            else:
                right = curr
                r_head = curr
            right = right.next
        curr = curr.next
    if l_head is None:
        return r_head
    left.next = r_head
    return l_head

def partition2(head, x):
    curr = head
    h = curr
    t = curr

    while curr:
        next = curr.next
        if curr.data < x:
            curr.next = h
            h = curr
        else:
            t.next = curr
            t = curr
        curr = next
    t.next = None
    return h
    

