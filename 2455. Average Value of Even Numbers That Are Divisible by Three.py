from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            if i % 6 == 0:
                arr.append(i)
        if len(arr) == 0:
            return 0
        else:
            return sum(arr)//len(arr)