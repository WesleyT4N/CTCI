from collections import deque

def list_of_depths(root):
    depths = {}
    res = {}
    d = 0
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if depths[d]:
            depths[d] += 1
        else:
            depths[d] = 1
        if res[d]:
            head = res[d][0]
            tail = res[d][1]
            tail.next = LLNode(curr.data)
            res[d] = [res[d][0], tail.next]
        else:
            head = LLNode(curr.data)
            res[d] = [head, head]
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        if depths[d] == 2 ** d:
            d += 1

    return list(map(lambda: x: x[0], [v for k, v in res]))


def linked_list_add_rec(h,data):
    if h:
        h.next = linked_list_add_rec(h.next, data)
        return h
    else:
        return Node(data)

