from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr = []
        for account in accounts:
            x = sum(account)
            arr.append(x)
        return max(arr)