class Solution:
    def pivotInteger(self, n: int) -> int:
        
        total_sum = (1+n)*n/2

        preSum, postSum = 0, total_sum
        i = 0
        while preSum < postSum:
            i+=1
            preSum += i
            postSum -= (i-1)
        
        if preSum == postSum:
            return i
        else:
            return -1
