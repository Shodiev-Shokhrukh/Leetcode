from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = 0
        arr = []
        for i in nums:
            x = x + i
            arr.append(x)
        return arr