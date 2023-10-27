class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_quadrat_sum(x):
            total = 0
            while x > 0:
                total += (x % 10)*(x % 10)
                x //= 10
            return total
        
        seen = set() 

        while n != 1 and n not in seen:
            seen.add(n) 
            n = digit_quadrat_sum(n)

        return n == 1