# reverse the nodes of the linked list in place and return the new head 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)

A.next = B
B.next = C
C.next = D
# D's next is null

# A -> B -> C -> D -> NULL
# NULL <- A <- B <- C <- D
def reverse(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

# print(reverse(A).value)

def reverseR(head, prev = None):
    if head == None:
        return prev
    next = head.next
    head.next = prev
    return reverseR(next, head)

print(reverseR(A).value)
    
    