# given a tree and an integer l, print values of tree at level l

from collections import deque
from implementation import genTree

def levelValues(root, l):
    if root is None:
        return None
    
    queue = deque()
    queue.append(root)
    level = 0

    while len(queue) > 0:
        level_size = len(queue)
        while level_size > 0:
            current = queue.popleft()
            # queue holds nodes of the next level in advance
            if level == l - 1:
                print(current.value)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

            level_size -= 1

        level += 1

levelValues(genTree(), 3)