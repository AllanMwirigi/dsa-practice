# check if target exists in tree
# do an OR check for each subtree
from collections import deque
from implementation import genTree

def dfs(node, target):
    if node is None:
        return False 
    if node.value == target:
        return True

    return dfs(node.left, target) or dfs(node.right, target)

def bfs(root, target):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        current = queue.popleft()
        if current.value == target:
            return True
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    
    return False

root = genTree()
print(dfs(root, 7))
print(bfs(root, 7))