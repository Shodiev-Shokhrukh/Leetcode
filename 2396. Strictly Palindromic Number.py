class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        if n == 4:
            return False

        def convert_n_base(number, base):
            if number == 0:
                return "0"
            result = ""
            while number > 0:
                remainder = number % base
                result = str(remainder) + result
                number //= base
            return result

        def is_palindrome(x):
            return x == x[::-1]

        for i in range(2, n - 1):
            representation = convert_n_base(n, i)
            if not is_palindrome(representation):
                return False
        return True