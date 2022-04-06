# given array of random numbers, push all zeros to end of array
# use O(n) Time and O(1) Space

def zerosToEnd(arr = []):
    n = len(arr)
    index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[index] = arr[i]
            index += 1

    # all non-zero elements have been shifted to front and 'index' is set as index of first 0. 
    # Make all elements from count to end to be zero
    while index < n:
        arr[index] = 0
        index += 1

    return arr

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
print(zerosToEnd(arr))
