class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count  = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            else:
                count[num] +=1