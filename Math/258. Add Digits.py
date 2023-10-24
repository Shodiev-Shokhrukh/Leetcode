class Solution:
    def addDigits(self, num: int) -> int:
        
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        total = digit_sum(num)
        while total> 9:
            total = digit_sum(total)

        return total 
            