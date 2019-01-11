def build_directed_graph(dependencies):
    if not dependencies:
        return []
    res = {}
    for edge in dependencies:

        start = edge[1]
        end = edge[0]
        if start in res:
            res[start].add(end)
        else:
            res[start] = {end}
    return res

def find_end(graph, node, visited):
    visited.add(node)
    if node not in graph:
        res = [node]
    else:
        res = []
        for neighbor in graph[node]:
            if neighbor not in visited:
                res += find_end(graph, neighbor, visited)
    return res

def remove_node(graph, node, build_order, to_be_added):
    for project in list(graph):
        if project in graph and node in graph[project]:
            graph[project].remove(node)
            if graph[project] == set():
                del graph[project]
                if graph == {}:
                    build_order.append(project)
                    to_be_added.remove(project)  


def build_order(projects, dependencies):
    graph = build_directed_graph(dependencies)
    stack = projects
    build_order = []
    to_be_added = set(projects)
    while stack:
        curr = stack.pop()
        if curr in to_be_added:
            if curr not in graph:
                build_order.append(curr)
                to_be_added.remove(curr)
                remove_node(graph, curr, build_order, to_be_added)
            else: 
                visited = set()
                res = find_end(graph, curr, visited)
                for p in res:
                    build_order.append(p)
                    to_be_added.remove(p)
                    remove_node(graph, p, build_order, to_be_added)
    return build_order

# projects = ['a', 'b', 'c', 'd', 'e', 'f']
# dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
projects = ['a', 'b', 'c']
dependencies = [('a', 'b'), ('b', 'c'), ('c', 'a')]
print(build_order(projects, dependencies))