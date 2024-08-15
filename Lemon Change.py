class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change5 = 0
        change10 = 0

        for bill in bills:
            if bill == 5:
                change5 +=1
            elif bill == 10:
                if change5 < 1:
                    return False
                else:
                    change5 -=1
                    change10 +=1
            else:
                #bill = 20
                #change = 15

                # 2 ways: 5+5+5 and 10 + 5 greedy checks for 10 + 5 first

                if change10 > 0 and change5 > 0:
                    change5 -=1
                    change10 -=1
                elif change5 >= 3:
                    change5 -=3
                else:
                    return False 


        return True