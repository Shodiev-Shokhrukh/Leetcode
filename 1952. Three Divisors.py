class Solution:
    def isThree(self, n: int) -> bool:
        arr = []
        for i in range(1, n+1):
            if n%i == 0:
                arr.append(i)
        return len(arr) == 3