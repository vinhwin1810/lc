class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ""
        index = word.find(ch)

        if index != -1:
            for i in range(index, -1, -1):
                res += word[i]

            for j in range(index+1,len(word)):
                res+= word[j]
            
            return res
        else:
            return word


        