from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for i in range(left, right+1):
            num_str = str(i)
            is_self_dividing = True
            for digit in num_str:
                if digit == '0' or i % int(digit) !=0:
                    is_self_dividing = False
                    break
            if is_self_dividing:
                arr.append(i)
        return arr