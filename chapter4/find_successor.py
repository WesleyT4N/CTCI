def rec_left(root):
    if root.left is None:
        return root
    return rec_left(root.left)

def find_successor(root):
    if root is None:
        return None
    if root.right:
        return rec_left(root.ight)
    q = root
    p = root.parent
    # we've traversed p's subtrees, so go to p
    while (p is not None and p.left != q):
        q = p
        p = p.parent
    return p