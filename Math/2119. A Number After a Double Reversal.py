class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a = str(num)
        s1 = int(a[::-1])
        s2 = str(s1)
        return int(s2[::-1]) == int(a)