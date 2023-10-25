class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split(" ")
        a = []

        for i in x:
            a.append(i[::-1])
        b = ' '.join([str(elem) for elem in a])
        return b