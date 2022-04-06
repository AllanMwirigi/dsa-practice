# given a directed graph, make a deep copy of it so that the cloned graph has the same vertices and edges as the original graph.

# do depth first traversal
# use a hashmap to track already cloned node to prevent recreation

# at each node; clone the node
# loop node neighbours; set neighbours in cloned node

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

def cloneGraph(node: Node):
    if node is None:
        return None

    clone = Node(node.value)

    for neighbour in node.neighbours:
        clone.neighbours.append(cloneGraph(neighbour))      

    return clone

def cloneGraph2(node: Node, clones = {}):
    if node is None:
        return None

    if node in clones:
        return clones[node]

    clone = Node(node.value)
    clones[node] = clone

    for neighbour in node.neighbours:
        clone.neighbours.append(cloneGraph(neighbour))      

    return clone





    