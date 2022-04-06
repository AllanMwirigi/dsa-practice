# determine if there is a path between the source and destination

# Time: O(e) - travel through every single edge
# Space: O(n)
#  n - num nodes, e - num edges

from creategraph import createGraph
from collections import deque

def hasPath(graph, src, dest):
    if src == dest:
        return True
    queue = deque()
    queue.append(src)
    while len(queue):
        current = queue.popleft()
        if current == dest:
            return True
        for neighbour in graph[current]:
            queue.append(neighbour)

    return False

def hasPathR(graph, src, dest):
    if src == dest:
        return True

    for neighbour in graph[src]:
        if hasPathR(graph, neighbour, dest) is True:
            return True

    return False

graph = createGraph()
print(hasPath(graph, 'a', 'e'))
print(hasPathR(graph, 'b', 'e'))