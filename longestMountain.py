from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        max_len = 0
        i = 1  # Start from the second element to avoid index out-of-range
        
        while i < n - 1:
            # Check if arr[i] is a peak
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                # Initialize left and right pointers for expansion
                left = i - 1
                right = i + 1
                
                # Expand to the left
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1
                
                # Expand to the right
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                
                # Calculate the length of the current mountain
                current_len = right - left + 1
                max_len = max(max_len, current_len)
                
                # Move i to the end of this mountain to avoid redundant checks
                i = right
            else:
                # Move to the next element if current is not a peak
                i += 1
        
        return max_len
