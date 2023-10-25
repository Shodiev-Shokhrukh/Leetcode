class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        word_dict = {}
        for word in words:
            for char in word:
                if char.isdigit():
                    word_dict[int(char)] = word[:-1]

        # Reconstruct the sentence with sorted words
        result = ' '.join(word_dict[i] for i in range(1, len(words) + 1))
        return result