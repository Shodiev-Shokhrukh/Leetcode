class Solution:
    def minimizedStringLength(self, s: str) -> int:
        x = set()
        for i in s:
            if i not in x:
                x.add(i)
        return len(x)