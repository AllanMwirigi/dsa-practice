# https://youtu.be/fAAZixBzIAI
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(6)

A.left = B
A.right = C
B.left = D
B.right = E
C.right = F

def genTree():
    return A

#         1
#     2           3
# 4       5           6