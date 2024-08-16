class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)

        curMin, curMax = arrays[0][0], arrays[0][-1]
        max_distance = 0

        for i in range(1, m):
            # Update max_distance considering the current array
            max_distance = max(max_distance, abs(arrays[i][-1] - curMin), abs(curMax - arrays[i][0]))

            # Update curMin and curMax
            curMin = min(curMin, arrays[i][0])
            curMax = max(curMax, arrays[i][-1])

        return max_distance


