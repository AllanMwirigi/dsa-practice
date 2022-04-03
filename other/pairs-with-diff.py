# Given an array of distinct integer values, count the number of pairs of integers that
# have difference k. F

def countPairs(arr = [], k = 2):
    elem_set = set()
    counter = 0
    for i in range(0, len(arr)):
        lower = arr[i] - k
        upper = arr[i] + k
        if lower in elem_set:
            counter += 1
        if upper in elem_set:
            counter += 1

        elem_set.add(arr[i])
    
    print(counter)

arr = [1, 7, 5, 9, 2, 12, 3]
countPairs(arr, 2)