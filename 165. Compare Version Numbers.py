class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        i, j = 0, 0

        while i < len(version1) or j < len(version2):
            revision1 = 0
            revision2 = 0

            while i < len(version1) and version1[i] != ".":
                revision1 = revision1 * 10 + int(version1[i])
                i+=1
            i+=1

            while j < len(version2) and version2[j] != ".":
                revision2 = revision2 * 10 + int(version2[j])
                j+=1
            j+=1
            if revision1 < revision2:
                return -1
            elif revision1 > revision2:
                return 1
        return 0  


            