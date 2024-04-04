class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}

        for i in range(len(s)):
            if s[i] not in map:
                if t[i] in map.values():
                    return False
                map[s[i]] = t[i]
                
            else:
                if t[i] != map[s[i]]:
                    return False
        
        return True