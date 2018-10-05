class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def minimal_tree(l):
    if len(l) == 0:
        return None
    mid = len(l)/2
    root = Node(l[mid])
    root.left = minimal_tree(l[:mid])
    root.right = minimal_tree(l[mid+1:])
    return root

def print_tree(t):
    if t is None:
        return
    print(t.data)
    print_tree(t.left)
    print_tree(t.right)

print_tree(minimal_tree([1,2,3,4,5,6,7,8]))