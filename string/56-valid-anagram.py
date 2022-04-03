# https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(s = '', t = ''):
    if len(s) != len(t):
        return False

    sDict = {}
    tDict = {}
    for i in range(len(s)):
        sDict[s[i]] = 1 + sDict.get(s[i], 0)
        tDict[t[i]] = 1 + tDict.get(t[i], 0)

    # similar to doing a loop comparing each key
    if sDict != tDict:
        return False

    return True

print(isAnagram(s = "anagram", t = "nagaram"))
print(isAnagram(s = "rat", t = "car"))
