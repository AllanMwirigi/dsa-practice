# use queue; set initial node
# while queue not empty
#   pop current node
#   add neighbours of current node to back of queue

from creategraph import createGraph
from collections import deque

def breadthFirst(graph, start='a'):
    if graph is None: return []
    queue = deque()
    queue.append(start)
    values = []

    while len(queue) > 0:
        current = queue.popleft()
        values.append(current)
        for neighbour in graph[current]:
            queue.append(neighbour)
        
    return values

graph = createGraph()
print(breadthFirst(graph))