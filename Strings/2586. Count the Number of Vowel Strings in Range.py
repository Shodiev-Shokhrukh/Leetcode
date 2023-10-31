from typing import List
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        wowels = ['a', 'i', 'u', 'e', 'o']
        count = 0
        for i in range(left, right+1):
            if words[i][0] in wowels and words[i][-1] in wowels:
                count += 1
        return count
