class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_length = 1
        length = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1
        
        return max(max_length, length)