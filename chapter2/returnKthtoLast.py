def kth_to_last(head, k):
    curr = head
    runner = head
    size = 0
    while runner:
        size += 1
        runner = runner.next
    i = 0
    while i < size - k:
        curr = curr.next
        i += 1
    return curr