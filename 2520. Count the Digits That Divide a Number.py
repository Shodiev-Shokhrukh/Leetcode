class Solution:
    def countDigits(self, num: int) -> int:
        x = 0
        for i in str(num):
            if num % int(i) == 0:
                x = x + 1

        return x