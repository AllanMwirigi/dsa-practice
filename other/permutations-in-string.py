# Given a smaller string s and a bigger string b, design an algorithm to find all permutations of the shorter string 
# within the longer one. Print the location of each permutation.
# similar to https://leetcode.com/problems/find-all-anagrams-in-a-string/

# invalid! - does not account for overlapping substrings that match s
def findPermutations2(s = '', b = ''):
    locations = []
    startIndex = -1
    bDict = dict()
    for elem in s:
        if elem not in bDict:
            bDict[elem] = 1
        else:
            bDict[elem] += 1
    
    bDictCopy = dict(bDict)

    for i, c in enumerate(b):
        if c in bDict:
            if startIndex == -1:
                locations.append(i)
                startIndex = i
            bDict[c] -= 1
            if bDict[c] == 0:
                del bDict[c]
            if len(bDict) == 0:
                bDict = dict(bDictCopy)
                startIndex = -1
        
        else:
            if startIndex != -1:
                bDict = dict(bDictCopy)
                startIndex = -1
                locations.pop()

    return locations

print(findPermutations2('abbc', 'cbabadcbbabbcbabaabccbabc'))