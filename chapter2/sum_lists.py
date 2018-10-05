def sum_lists(l1. l2):
    h = None:
    carry = 0
    curr = h
    while l1 or l2:
        sum = carry
        if l1:
            sum += l1.data
        if l2:
            sum += l2.data
        if sum // 10 !== 0:
            carry = sum % 9
        else:
            carry = 0
        if h:
            curr.next = sum % 10
        else:
            h = Node(sum)
            curr = h
        curr = curr.next

def sum_lists_rec(l1, l2, carry):
    if l1 is None and l2 is None and carry == 0:
        return null
    res = Node()
    val = carry
    if l1:
        val += l1.data
    if l2:
        val += l2.data
    c = 0
    if val >= 10:
        c = 1
    res.data = val % 10
    if (l1 is not None or l2 is not None):
        if l1 and l2:
            rest = sum_lists_rec(l1.next, l2.next, c)
        else if l1:
            rest = sum_lists_rec(l1.next, None, c)
        else if l2:
            rest = sum_lists_rec(None, l2.next, c)
        else:
            rest = None
        res.next = rest
    return res

def len_of_ll(l):
    count = 0
    curr = l
    while curr:
        count += 1
        curr = curr.next
    return count

def insert_before(h, data):
    new = node(data)
    new.next = h
    return new

def pad_zero(l, zero_count):
    count = 0
    curr = l
    while (count < zero_count)
        curr = insert_before(curr, 0)
        count += 1
    return curr



class PartialSum:
    def __init__():
        self.sum = None
        self.carry = 0

def add_list_helper(l1, l2)
    if l1 is None and l2 is None:
        return PartialSum()
    sum = add_list_helper(l1.next, l2.next)
    val = sum.carry + l1.data + l2.data 
    full_result = insert_before(sum.sum, val % 10)
    sum.sum = full_result
    sum.carry = val // 10
    return sum

def sum_rev(l1, l2):
    l1_len = len_of_ll(l1)
    l2_len = len_of_ll(l2)

    if l1_len < l2_len:
        pad_zero(l1, l2_len - l1_len)
    else:
        pad_zero(l2, l1_len - l2_len)
    
    partial_sum = add_list_helper(l1, l2)
    if partial_sum.carry != 0:
        partial_sum.sum = insert_before(partial_sum.sum, partial_sum.carry)
    return partial_sum.sum

