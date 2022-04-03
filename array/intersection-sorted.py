# Given two sorted arrays, find the number of elements in common. The arrays are the same length
# and each has all distinct elements.

# Considerations - O(n) time and O(1) space, account for duplicates
                # negative values, single value lists, 0's, and empty list arguments.
# so need to search the array without a hashmap; 
# for loop of one array with binary search of the other would be O(nlogn)
# but don't need a full binary search, since it is just from the last match, so it can be a linear search

# O(n) time and O(1) space
def intersect(l1 = [], l2 = []):
    i, j = 0, 0
    result = []

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            result.append(l1[i])
            i += 1
            j += 1

    return result

A = [1, 2, 3, 3, 4, 5, 6]
B = [3, 3, 5]
print(intersect(A, B))