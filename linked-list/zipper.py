# given two linked lists, need to zipper them
# reassign the next pointers in place such that they alternate between the nodes of the two lists
# each list is non empty

# start with the first node
# if one is longer than the other, alternate to the limit, then finish off with the remaining nodes of the longer

def zipper(head1, head2):
    current1 = head1
    current2 = head2
    tail = None
    count = 0
    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            if tail is not None: tail.next = current1
            tail = current1
            current1 = current1.next
        if count % 2 != 0:
            tail.next = current2
            tail = current2
            current2 = current2.next
            
        count += 1

    if count % 2 == 0:
        tail.next = current1
    if count % 2 != 0:
        tail.next = current2

    return head1

def zipperR(head1, head2):
    if head1 is None and head2 is None: return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = zipperR(next1, next2)
    return head1


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

A = Node(0)
B = Node(2)
C = Node(4)
D = Node(6)
E = Node(8)

A.next = B
B.next = C
C.next = D
D.next = E

F = Node(1)
G = Node(3)
H = Node(5)

F.next = G
G.next = H

from implement import traverse
node = zipperR(A, F)
traverse(node)

# 0 -> 2 -> 4 -> 6 -> 8
# 1 -> 3 -> 5
# 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8

# track current node for each list - current1 = head1, current2 = head2
# track the tail node of the combined list - tail
# track count
# iterate while current1 and current2 are not null
#   count even
#       if tail is not null: tail.next = current1
#       tail = current1
#       current1 = current1.next
#       inc count
#   count odd
#       tail.next = current2
#       tail = current2
#       current2 = current2.next
#       inc count

#   count even
#       tail.next = current1
#   count odd
#       tail.next = current2

# tail - 5
# current1 - 6
# current2 - null
# count = 4
# 0 -> 1 -> 2 -> 3 -> 4 -> 5

