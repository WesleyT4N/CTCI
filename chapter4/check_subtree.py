def preorder_append(t, s):
    if t is None:
        return s + [None]
    s.append(t.data)
    s = preorder_append(t.left, s)
    s = preorder_append(t.right, s)
    return s

def check_subtree(t1, t2):
    preorder_t1 = preorder_append(t, [])
    preorder_t2 = preorder_append(t, [])

    i = 0
    while i < len(preorder_t1):
        if preorder_t1[i] != preorder_t2[0]:
            i += 1
        else:
            return preorder_t1[i:] == preorder_t2
    return False

def match_tree(t1, t2):
    if t1 is None and t2 is None:
        return True
    else if t1 is None or t2 is None:
        return False
    else if t1.data != t2.data:
        return False
    return match_tree(t1.left,  t2.left) and match_tree(t1.right, t2.right)

def check_subtree_rec(t1, t2):
    if t2 is None:
        return True
    if t1 is None:
        return False
    else if t1.data == t2.data and match_tree(t1, t2):
        return True
    return check_subtree(t1.left, t2) or check_subtree(t1.right, t2)