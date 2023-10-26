class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        letter_to_number = {
            'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4',
            'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'
        }

        def get_numeric_value(word):
            return ''.join(letter_to_number[letter] for letter in word)

        numeric_first = get_numeric_value(firstWord)
        numeric_second = get_numeric_value(secondWord)

        numeric_target = get_numeric_value(targetWord)

        return int(numeric_first) + int(numeric_second) == int(numeric_target)
