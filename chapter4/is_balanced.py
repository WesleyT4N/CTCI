INT_MIN = -999999999

def is_balanced(root):
    if root is None:
        return False
    res = get_height(root)
    return res != INT_MIN


def get_height(root):
    if root is None:
        return -1
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    if abs(left_height - right_height) > 1:
        return INT_MIN
    return max(left_height, right_height) + 1


