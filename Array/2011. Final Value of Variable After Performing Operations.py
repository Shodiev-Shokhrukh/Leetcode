from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        minus_count = 0
        plus_count = 0
        for i in operations:

            if i == '--X' or i== 'X--':
                minus_count += 1
            else:
                plus_count += 1
        return plus_count - minus_count
