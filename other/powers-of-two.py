# prints the powers of 2 from 1 through n (inclusive). For example, if n is 4, it would
# print 1, 2, and 4.

def findPowers2(n, result = []):
    if n <= 0:
        result.append(0)
    num = 1
    while num <= n:
        result.append(num)
        num *= 2

    print(result)

def findPowers2Recursive(n):
    if n < 1:
        # takes care of odd n
        return 0
    if n == 1:
        print(n)
        return 1
    # half = -(-n//2)
    prev = findPowers2Recursive(n/2)
    current = prev * 2
    print(current)
    return current

# findPowers2(16)
findPowers2Recursive(99)