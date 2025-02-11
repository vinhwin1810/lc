209. Minimum Size Subarray Sum

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float("inf")  # Renamed from max_len to min_len (better naming)

        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]  # Add nums[j] before checking condition
                
                if cur_sum >= target:  # Once we reach target, update min_len
                    min_len = min(min_len, j - i + 1)
                    break  # Stop early to minimize length
        
        return min_len if min_len != float("inf") else 0  # Handle no valid subarray case

