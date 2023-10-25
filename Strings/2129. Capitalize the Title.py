class Solution:
    def capitalizeTitle(self, title: str) -> str:
        x = title.split(" ")
        a = []

        for i in x:
            if len(i) <3:
                a.append(i.lower())
            else:
                a.append(i.lower().capitalize())
        b = ' '.join([str(elem) for elem in a])
        return b