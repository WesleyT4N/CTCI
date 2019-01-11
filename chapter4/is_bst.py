
def check(root, min, max):
    if root is None:
        return True
    if min is not None and root <= min:
        return False
    if max is not None and root > max:
        return False
    return check(root.left, min, root.value) and check(root.right, root.value, max)


def is_bst(root):
    if root is None:
        return True
    return check(root.left, None, root.value) and check(root.right, root.value, None)