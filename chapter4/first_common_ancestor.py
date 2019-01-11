class Result:
    def __init__(self, node=None, is_ancestor=False):
        self.node = node
        self.is_ancestor = is_ancestor

def common_anc_helper(root, node1, node2):
    if root is None:
        return Result()
    if root is node1 and root is node2:
        return Result(root, True)
    
    in_left = common_anc_helper(root.left, node1, node2)
    if in_left.is_ancestor:
        return in_left
    
    in_right = common_anc_helper(root.right, node1, node2)
    if in_right.is_ancestor:
        return in_right

    # this is the common acnestor
    if in_left.node and in_right.node:
        return Result(root, True)
    # accounts for if node1 is an ancestor of node2
    if root is node1 or root is node2:
        is_ancestor = in_left is not None or in_right is not None
        return Result(root, is_ancestor)
    # We've found one of the two nodes, bubble up
    if in_left.node:
        return Result(in_left.node, False)
    return Result(in_right.node, False)

def first_common_ancestor(root, node1, node2):
    result = common_anc_helper(root, node1, node2)
    if result.is_ancestor:
        return r.node
    return None