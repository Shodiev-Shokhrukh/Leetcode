class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        for i in str(n):
            sum = sum + int(i)
            product = int(i)*product
        
        return product - sum