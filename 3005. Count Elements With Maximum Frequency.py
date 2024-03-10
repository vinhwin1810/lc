class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count  = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] +=1
        
        values = []
        for val in count.values():
            values.append(val)
        
        maxFreq = max(values)
        res = 0
        print(count)
        for key in count.keys():
            if count[key] == maxFreq:
                res+=maxFreq
        return res
        


