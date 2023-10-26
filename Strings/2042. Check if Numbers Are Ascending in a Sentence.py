class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(w) for w in s.split() if w.isdigit()]
        return all(nums[i-1] < nums[i] for i in range(1, len(nums)))