class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == 0:
                return nums[j]
            elif nums[i] + nums[j] < 0:
                i+=1
            else:
                j-=1
        
        return -1
