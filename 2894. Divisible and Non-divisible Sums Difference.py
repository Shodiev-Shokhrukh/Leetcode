class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1 = 0
        sum2 = 0
        for i in range(1, n+1):
            if i % m == 0:
                sum1 = sum1 + i
            sum2 = sum2  + i
        return sum2 - 2*sum1