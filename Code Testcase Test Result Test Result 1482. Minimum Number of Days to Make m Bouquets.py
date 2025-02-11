class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        #Sliding window approach
        n = len(nums)
        min_len = float("inf")
        left = 0
        cur_sum = 0

        for right in range(n):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        
        return min_len if min_len != float("inf") else 0
