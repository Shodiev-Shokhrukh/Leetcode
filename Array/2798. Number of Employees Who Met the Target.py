from typing import List
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        a = 0
        for i in range(0, len(hours)):
            if hours[i] >= target:
                a += 1
        return a