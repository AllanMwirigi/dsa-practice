# use stack; set initial node
# while stack not empty
#   pop current node
#   add neighbours of current node to stack

from creategraph import createGraph

def depthFirst(graph, start='a'):
    if len(graph) == 0:
        return []
    stack = [start]
    values = []
    while len(stack) > 0:
        current = stack.pop()
        values.append(current)
        neighbours = graph[current]
        for n in neighbours:
            stack.append(n)

    return values

def depthFirstR(graph, start='a'):
    print(start)
    for neighbour in graph[start]:
        depthFirstR(graph, neighbour)

graph = createGraph()
print(depthFirst(graph))
depthFirstR(graph, 'a')

