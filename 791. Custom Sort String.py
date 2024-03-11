#Medium:
#Hash table or Sorting

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}

        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
        
        res = ""
        for i in order:
            if i in count:
                freq = count[i]
                for _ in range(freq):
                    res += i
                    count[i] -= 1
        
        for char, freq in count.items():
            while freq != 0:
                res += char
                freq -=1
        
        return res
        
