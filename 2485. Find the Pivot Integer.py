class Solution:
    def pivotInteger(self, n: int) -> int:
        s1 = 0
        s2 = 0
        for i in range(1,n+1):
            s1 = sum(range(1, i+1))
            s2 = sum(range(i, n+1))
            if(s1==s2):
                return i
        return -1
