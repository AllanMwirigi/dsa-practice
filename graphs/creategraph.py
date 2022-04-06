# https://youtu.be/tWVWeAqZ0WU
# adjacency list - mapping of node to neighbour(s)
def createGraph():
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    return graph

# directed graph has arrows or directive paths and can't go back in opp dir of arrow
# acyclic graph has no cycles i.e. is guaranteed to terminate
# path like a -> b -> c -> a is cyclic and would traverse infinitely