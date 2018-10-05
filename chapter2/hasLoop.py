def loopDetection(l):
    slow = l
    fast = l.next.next
    collision = None
    while slow.next and fast.next.next:
        if slow is fast:
            collision = slow
        slow = slow.next
        fast = fast.next.next
    slow = l
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow