class Solution:
    def totalMoney(self, n: int) -> int:
        res,k = 0,0

        for i in range(n):
            k = 1 + i//7
            res += k + (i%7)
        return res
            
