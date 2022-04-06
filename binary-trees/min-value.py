# https://www.youtube.com/watch?v=fAAZixBzIAI&list=PLAIXm3ZmkXBoe0m-86RYHmMwmnz_3riuz&index=3
from implementation import genTree

def minValue(root):
    if root is None:
        # no node after leaves on final level;
        # need to return sth that can't be minimum compared to actual nodes i.e. +infinity
        return float('inf') # -ve infinity is float('-inf')

    return min(
        root.value,
        minValue(root.left),
        minValue(root.right)
    )

root = genTree()
print(minValue(root))