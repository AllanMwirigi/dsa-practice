# travel across level before going deeper
# A, B, C, D, E, F -> 1, 2, 3, 4, 5, 6
# use queue with root initial
# check if queue empty; 
#   remove top elem, set as current
#   check children of current, add to queue starting with left child
# Time: O(n) - each node visited; if queue used has constant time add and remove
# Space: O(n) - at most n nodes added

from collections import deque
from implementation import genTree

def breadthFirst(root):
    if root is None: return []
    queue = deque()
    queue.append(root)
    values = []
    while len(queue) > 0:
        current = queue.popleft()
        values.append(current.value)
        # ensure to add the left first
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return values    

root = genTree()
print(breadthFirst(root))
    