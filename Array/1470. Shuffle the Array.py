from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(0, n):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr