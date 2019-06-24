# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest 
# substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_set = set()
        i = 0
        p_i = 0
        while i < len(s):
            if s[i] in s[p_i:i]:
                substr_set |= {len(s[p_i:i])}
                p_i += 1
            else:
                i += 1
        else:
            substr_set |= {len(s[p_i:i])}
        if len(substr_set) == 0:
            t = 0
        else:
            t = max(substr_set)
        return t