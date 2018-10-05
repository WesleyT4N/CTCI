class Helper:
    def __init__(self, node, len=0):
        self.node = None
        self.len = len

def tail(l, len):
    if l.next is None:
        return Helper(l, len)
    return tail(l.next, len+1)

def intersection(l1, l2):
    if l1 is None or l2 is None:
        return None
    t1 = tail(l1, 0)
    t2 = tail(l2, 0)
    if t1.node is not t2.node:
        return None

    if t1.node is not None:
        t1.len += 1
    if t2.node is not None:
        t2.len += 1

    len_diff = abs(t1.len - t2.len)

    p1 = l1
    p2 = l2
    while len_diff > 0:
        if t1.len > t2.len:
            p1 = l1.next
        else:
            p2 = l2.next
    
    while p1 is not p2:
        p1 = p1.next
        p2 = p2.next
    return p1;