class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashNums = set(nums)

        max_length = 0
        for i in hashNums:
            if i - 1 not in hashNums:
                length = 1
                while i + length in hashNums:
                    length += 1
                max_length = max(max_length, length)
            
        return max_length
