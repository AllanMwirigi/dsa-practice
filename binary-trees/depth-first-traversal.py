# start with root node, add to collection
# need to go deeper in the tree before moving laterally
# A, B, D, E, C, F - maintain in order - 1, 2, 4, 5, 
# use stack; initially with the root node
# pop stack; add current node value to values list; check children
# if exists, first add right child of current node to stack, then left
# stack empty means completed
# T - O(n) where n is num of nodes; each node visited
# S - O(n) - at most n nodes added to stack

from implementation import genTree

def depthFirst(root):
    if root is None: return []
    stack = [root]
    values = []
    while len(stack) != 0:
        current = stack.pop()
        values.append(current.value)
        # ensure to add the right one first, since it should be removed first
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return values

def depthFirstR(root):
    if root is None: return []
    left_values = depthFirstR(root.left) # [2, 4, 5]
    right_values = depthFirstR(root.right) # [3, 6]
    return [root.value] + left_values + right_values # 1, 2, 4, 5, 3, 6

root = genTree()
print(depthFirst(root))
print(depthFirstR(root))
