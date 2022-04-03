# say that you are a traveller in a 2D grid. Begin at top left corner and goal is to get to bottom right
# can only move down or right
# in how many ways can you get to the goal in a grid of dimensions m * n

def gridTraveler(m, n, memo = dict()):
    key = str(m) + ',' + str(n)
    if key in memo: return memo[key]
    key2 = str(n) + ',' + str(m)
    # if key in memo or key2 in memo: return memo[key] 
    if m == 0 or n == 0: return 0 # grid is empty, no way to traverse
    if m == 1 and n == 1: return 1 # can only move one way
    # cannot move diagonally based on rules i.e. gridTraveler(m - 1, n - 1)
    memo[key] =  gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
    # memo[key2] = memo[key]
    return memo[key]

print(gridTraveler(18, 18))