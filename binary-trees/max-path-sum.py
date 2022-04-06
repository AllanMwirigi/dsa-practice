# https://www.youtube.com/watch?v=fAAZixBzIAI&list=PLAIXm3ZmkXBoe0m-86RYHmMwmnz_3riuz&index=3
# get the maximum sum of nodes on from the root to the leaf

from implementation import genTree

def maxPathSum(root):
    if root is None:
        # return sth that cannot be greater than parent
        return float('-inf')

    return max(root.value, max(
        root.value + maxPathSum(root.left), 
        root.value + maxPathSum(root.right)
    ))

def maxPathSum2(root):
    if root is None:
        return float('-inf')
    if root.left == None and root.right == None:
        # leaf node
        return root.value
    return root.value + max(
        maxPathSum2(root.left),
        maxPathSum2(root.right)
    )

root = genTree()
print(maxPathSum(root))
print(maxPathSum2(root))