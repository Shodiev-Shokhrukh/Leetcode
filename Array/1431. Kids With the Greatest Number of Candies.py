from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = max(candies)
        arr = []
        for i in candies:
            if i + extraCandies >= x:
                arr.append(True)
            else:
                arr.append(False)
        return arr