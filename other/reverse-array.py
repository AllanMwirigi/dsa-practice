def reverseArr(arr = []):
    n = len(arr)
    half = -(-n // 2) # round up any float result
    for i in range(0, half):
        val = arr[i]
        newPos = n - i - 1
        otherVal = arr[newPos]
        arr[i] = otherVal
        arr[newPos] = val

    print(arr)

reverseArr([1,2,3,4,5])