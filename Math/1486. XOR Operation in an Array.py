class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]  # Generate the array nums
        result = 0

        for num in nums:
            result ^= num  # Perform the XOR operation

        return result