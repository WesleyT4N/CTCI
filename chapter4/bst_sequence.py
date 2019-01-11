def weave(first, second, results, prefix):
    if len(first) == 0 or len(second) == 0:
        result = prefix
        results += result + first + second

    head_first = first.pop(0)
    prefix.append(head_first)
    weave(first, second, results, prefix)
    prefix.pop()
    first.insert(0, head_first)

    head_second = second.pop(0)
    prefix.append(head_second)
    weave(first, second, results, prefix)
    prefix.pop()
    second.insert(0, head_second)



def bst_sequence(root):
    result = []
    if root is None:
        return result
    prefix = [root.data]
    left = bst_sequence(root.left)
    right = bst_sequence(root.right)
    for l_seq in left:
        for r_seq in right:
            weaved = []
            weave_lists(left, right, weaved, prefix)
            result += weaved
    return result