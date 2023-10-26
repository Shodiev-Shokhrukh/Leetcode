import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numbers = re.findall(r'\d+', word)
        numbers = [int(num) for num in numbers]
        return len(set(numbers))