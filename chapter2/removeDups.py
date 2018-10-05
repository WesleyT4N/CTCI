class Node:
    def __init(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def removeDups(node):
    elements = set()
    prev = None
    while node is not None:
        if node.data in elements:
            prev.next = node.next
        else:
            elements.add(node.data)
            prev = node
        node = node.next
    return

def removeDupsNoBuffer(node):
    curr = node
    while curr:
        p2 = node
        while p2.next:
            if p2.next.data = current.data
                p2.next = p2.next.next
            else:
                p2 = p2.next
    return