class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        listString = s.split()
        return len(listString[-1])