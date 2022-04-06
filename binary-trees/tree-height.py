from implementation import genTree
from collections import deque

def treeHeight(root):
    if root is None:
        return 0

    return 1 + max(
        treeHeight(root.left),
        treeHeight(root.right)
    )

def treeHeight2(root):
    if root is None:
        return 0
    queue = deque()
    queue.append(root)
    levels = 0

    while len(queue) > 0:
        level_size = len(queue) # size of current level
        while level_size > 0:
            current = queue.popleft()
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

            level_size -= 1
        
        levels += 1

    return levels

root = genTree()
print(treeHeight(root))
print(treeHeight2(root))