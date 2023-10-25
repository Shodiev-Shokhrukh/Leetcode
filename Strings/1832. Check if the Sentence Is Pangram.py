import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = sentence.lower()
        alphabet_set = set(string.ascii_lowercase)
        for char in s:
            if char in alphabet_set:
                alphabet_set.discard(char)
        
        return not alphabet_set