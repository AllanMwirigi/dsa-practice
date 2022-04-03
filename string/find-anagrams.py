# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# https://www.youtube.com/watch?v=G8xtZy0fDKg

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# runtime is O(s)
def findAnagrams(s = '', p = ''):
    if len(p) > len(s): return []
    sDict = {}
    pDict = {}
    
    for c in p:
        pDict[c] = pDict.get(c, 0) + 1
        sDict[c] = sDict.get(c, 0) + 1

    result = [0] if pDict == sDict else []
    l = 0

    for r in range(len(p), len(s)):
        sDict[s[r]] = sDict.get(s[r], 0) + 1
        sDict[s[l]] -= 1

        if sDict[s[l]] == 0:
            sDict.pop(s[l])

        l += 1

        # comparing two dicts is an O(n) op. Hv, since there is a max of 26 possible chars, runtime is O(26) in this case
        if pDict == sDict:
            result.append(l)

    return result

print(findAnagrams("cbaebabacd", "abc"))
print(findAnagrams("abab", "ab"))

