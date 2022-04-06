from implementation import genTree

def treeSum(root):
    if root is None:
        return 0

    return root.value + treeSum(root.left) + treeSum(root.right)

root = genTree()
print(treeSum(root))