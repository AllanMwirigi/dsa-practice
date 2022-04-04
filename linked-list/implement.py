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

def traverse(head):
    current = head
    while current != None:
        print(current.value)
        current = current.next

def traverseR(head):
    if head is None:
        return
    print(head.value)
    traverseR(head.next)

# traverse(A)
# traverseR(A)

# Given head node of linked list, return array of values in order
def values(head):
    result = []
    current = head
    while current is not None:
        result.append(current.value)
        current = current.next

    return result

# print(values(A))

# Given head node of linked list, return sum of all values
def sum(head):
    if head is None: return 0
    return head.value + sum(head.next)

# print(sum(A))

# given linked list and target, determine whether target is present i.e. return true
def find(head, target):
    current = head
    while current is not None:
        if current.value == target:
            return True
        current = current.next
    
    return False

# print(find(A, 7))

# given linked list and an index, return the value at the index
def get(head, index):
    counter = 0
    current = head
    while current != None:
        if counter == index:
            return current.value
        current = current.next
        counter += 1

    return None

# print(get(A, 1))