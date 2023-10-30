from math import floor, ceil

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x = dividend / divisor
        if x < 0:
            return ceil(x)
        else:
            if floor(x) > pow(2, 31) -1:
                return floor(x) -1
            return floor(x)