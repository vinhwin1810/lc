class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for senior in details:
            age = senior[-4: -2]
            if int(age) > 60:
                count +=1
        
        return count