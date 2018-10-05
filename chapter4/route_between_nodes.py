from collections import deque

class Node:
    def __init__(self, data=None, neighbors=[]):
        self.data = data
        self.neighbors = neighbors

def route_between_nodes(node1, node2):
    if node1 is None or node2 is None:
        return []
    visited = {}
    queue = deque([node1])
    while len(queue) > 0:
        curr = queue.popleft()
        visited.add(curr)
        if curr is node2:
            return True
        for n in curr.neighbors:
            if n not in visited:
                queue.append(n)
    return False

def print_route_between_nodes(node1, node2):
    if node1 is None or node2 is None:
        return []
    queue = deque([start])
    while queue:
        path = queue.popleft()
        last_node = path[-1]
        if last_node == node2:
            return path
        for n in last_node.neighbors:
            new_path = path.copy()
            new_path.append(n)
            queue.append(new_path)