class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < 2 * k:
            return s[:k][::-1] + s[k:]
        else:
            return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k)
