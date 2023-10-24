from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0
        prod = 1
        for i in nums:
            prod = prod * i
        if prod < 0:
            return -1
        elif prod > 0:
            return 1
        return 0
        