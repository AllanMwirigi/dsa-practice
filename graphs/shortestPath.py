# determine shortest path between two nodes

# bfs, so queue 
# add both current node and its distance
# while adding neighbours to queue, inc distance based on current i.e. current's distance + 1
# also track visited for cyclic graph; anything added to the queue should be marked as visited

from collections import deque

def shortestPath(edges, node1, node2):
    graph = {} # TODO: build graph from edges
    queue = deque()
    queue.append([node1, 0])
    visited = set()
    visited.add(node1)

    while len(queue) > 0:
        current = queue.popleft()[0]
        distance = queue.popleft()[1]
        if current == node2:
            return distance
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append([neighbour, distance + 1])
                visited.add(neighbour)

    return -1
            
