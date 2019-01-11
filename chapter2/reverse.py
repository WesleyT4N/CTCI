class LinkedListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def print_list(self):
        curr = self
        s = "["
        while curr:
            s += "{}, ".format(curr.val)
            curr = curr.next
        s += "]"
        print(s)

def reverse(h):
    if h is None or h.next is None:
        return h
    head = h
    rest = reverse(head.next)
    head.next.next = head
    head.next = None
    return rest


a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
a.next = b
b.next = c
a.print_list()
reverse(a).print_list()