from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        x = ''
        for word in words:
            x = x + word[0]
        
        if x == s:
            return True
        else:
            return False
        