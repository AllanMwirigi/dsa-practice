# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from typing import OrderedDict


class Solution:

    def lengthOfLongestSubstring(self, s: str = "ggububgvfk") -> int: # O(n)
        # sliding window maintaining left and right pointer of window (substring)
        # create set; while looping forward check if elem exists in set
        # if elem in set (repeating char), go through the window removing elems until the prev match is removed
        # add current elem to set
        sbstrng = set()
        l = 0
        maxlength = 0

        for r in range(len(s)):
            while s[r] in sbstrng:
                # remove elems from the set, from the start of the window to the prev occurrence of this char 
                sbstrng.remove(s[l])
                l += 1
            sbstrng.add(s[r])
            maxlength = max(maxlength, r - l + 1)

        return maxlength


    def lengthOfLongestSubstring2(self, s: str = "ggububgvfk") -> int:
        # create hashmap; while looping forward add each elem to hashmap, if it does not already exist
        # if elem in hashmap (repeating char), set length of hashmap as maxlength if greater than prev substring
        # then clear prev occurrence and all elems before it; add current element
        # this approach is the sliding window, but using a complex and inefficient way to do the above clearing
        # "abcabcbb", "dvdkdef", "nfpdmpi", "aab"

        if len(s) == 0:
            return 0

        maxlength = 0
        inlength = 0
        sbstrng = OrderedDict()
        for i, char in enumerate(s):
            if char not in sbstrng:
                sbstrng[char] = i
                inlength = len(sbstrng)
            else:
                if inlength > maxlength:
                    maxlength = inlength
                # sbstrng.clear()
                a = next(iter(sbstrng.items()))[1] # original index of first elem in ordereddict; next(iter(...)) returns a tuple of the key-value pair
                b = sbstrng[char] # original index of existing occurrence of this character
                # remember that as you add/remove items the actual indexes change, but the difference will not
                delRange = b - a + 1 # intend to clear from start of dict to the existing occurrence
                sbstrng = OrderedDict(list(sbstrng.items())[delRange:]) # clear prev match and all before it
                sbstrng[char] = i

        if maxlength < inlength:
            # case where there are no repeating chars or last substring has no repeating chars e.g. "aab"
            # so never went to else block
            return inlength
        return maxlength

    def lengthOfLongestSubstring3(self, s: str = "abcabcbb") -> int: # O(n²)
        # add each elem to hashmap while looping forward, 
        # in inner loop, add elem to hashmap if it does not exist there
        # if elem exists (repaeating char), clear hashmap and break out of inner loop
        # set length of hashmap as maxlength if longer than prev substring

        if len(s) == 0:
            return 0

        maxlength = 0
        sbstrng = dict()
        for i, char in enumerate(s):
            sbstrng[char] = char
            inlength = 1
            for j in range(i+1, len(s)):
                char2 = s[j]
                if char2 not in sbstrng:
                    sbstrng[char2] = char2
                    inlength += 1
                else:
                    sbstrng.clear()
                    break
                    # sbstrng[char] = char
            
            if inlength > maxlength:
                maxlength = inlength

        return maxlength

maxlength =  Solution().lengthOfLongestSubstring()
print (maxlength)