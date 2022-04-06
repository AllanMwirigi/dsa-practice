# given list of edges of an undirected graph, determine whether there is a path between the source and destination nodes

# build adjecency list from list of edges; need to add both nodes in edge to each other
# e.g. [ i, j]  -> { i: [j], j: [i] }

# use a set to keep track of visited nodes to ensure that we don't get into cycles i.e. infinite loop

def hasPath(graph, src, dest, visited=set()):
    if src == dest:
        return True
    if src in visited:
        return False
    
    visited.add(src)

    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dest) == True:
            return True
    
    return False
