import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for i in range(0, len(s)):
            if s[i] == letter:
                count+=1
        return math.floor((count/len(s))*100)