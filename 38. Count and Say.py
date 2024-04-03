class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        previous_res = self.countAndSay(n-1)

        res = ""

        i = 1
        sub = previous_res[0]
        while i < len(previous_res):

            if previous_res[i] == sub[-1]:
                sub+=previous_res[i]
            else:
                res += str(len(sub))
                res+= sub[-1]
                sub = previous_res[i]
            i+=1
        
        res += str(len(sub))
        res+= sub[-1]

        return re
