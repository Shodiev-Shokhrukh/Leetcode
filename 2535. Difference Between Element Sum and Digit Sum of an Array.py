from typing import List
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_digits = sum(int(digit) for num in nums for digit in str(num))
        sum_numbers = sum([x for x in nums])
        if sum_digits > sum_numbers:
            return sum_digits - sum_numbers
        return sum_numbers - sum_digits