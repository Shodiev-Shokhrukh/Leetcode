from typing import List
from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_n = max(nums)
        min_n = min(nums)
        return gcd(max_n, min_n)