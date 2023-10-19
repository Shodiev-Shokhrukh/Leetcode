class Solution:
    def countEven(self, num: int) -> int:
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        count = 0
        for i in range(1, num + 1):
            if digit_sum(i) % 2 == 0:
                count += 1

        return count
