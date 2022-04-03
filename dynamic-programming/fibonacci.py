# implemented using memoization
# https://www.youtube.com/watch?v=oBt53YbR9Kk&list=WL&index=10&t=210s
# O(n) time and O(n) space
def fib(n, memo=dict()):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(50))