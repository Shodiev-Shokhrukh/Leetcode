class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alpha=['a','b','c','d','e','f','g','h']
        for i in range(len(alpha)):
            for j in range(1,9):
                if alpha[i]+str(j)==coordinates:
                    if (i+j)%2==0:
                        return True
        else:
            return False