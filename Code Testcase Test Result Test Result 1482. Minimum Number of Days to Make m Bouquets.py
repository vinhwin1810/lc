class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if m*k > n:
            return -1
        
        def canMake(day):
            flowers = 0
            bouquets = 0

            for bloom in bloomDay:
                if bloom <= day:
                    flowers +=1
                    if flowers == k:
                        bouquets +=1
                        flowers = 0
                        if bouquets >= m:
                            return True  # Early exit if required bouquets are met
                else:
                    flowers = 0
            
            return bouquets >= m
        

        l = min(bloomDay)
        r = max(bloomDay)

        while l < r:
            mid = (l+r) // 2

            if canMake(mid):
                r = mid
            else:
                l = mid + 1
        
        return l if canMake(l) else -1
