from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        x = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    x += 1
        return x