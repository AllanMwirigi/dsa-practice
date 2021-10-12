class Solution:
    def longestPalindrome(self, s: str = "madam") -> str: # O(n²) - dynamic programming?
        # https://www.youtube.com/watch?v=XYQecbcd6_c
        # for each character check for the longest palindrome where the char is the centre
        sbstrng = ""
        length = 0

        for i in range(len(s)):
            # odd length substring
            # take the current char as the centre and expand outwards   
            l, r = i, i
            # while l and r pointers are in bound and the chars between them form a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # update substring and its length
                if (r - l + 1) > length:
                    sbstrng = s[l:r+1]
                    length = r - l + 1
                # update the pointers
                l -= 1
                r += 1
            
            # even length substring e.g. cbbd
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    sbstrng = s[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1

        return sbstrng

print(Solution().longestPalindrome())

# O(n) - https://www.educative.io/edpresso/longest-palindromic-substring-in-on-with-manachers-algorithm