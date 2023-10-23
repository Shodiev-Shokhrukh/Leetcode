class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def convert_n_base(number, base):
            if number == 0:
                return "0"
            result = ""
            while number > 0:
                remainder = number % base
                result = str(remainder) + result
                number //= base
            return result

        def digit_sum(s):
            total = 0
            n = int(s)
            while n > 0:
                total += n % 10
                n //= 10
            return total
        return digit_sum(convert_n_base(n, k))