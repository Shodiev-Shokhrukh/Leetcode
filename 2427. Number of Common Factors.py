class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factors_a = [i for i in range(1, a + 1) if a % i == 0]
        factors_b = [i for i in range(1, b + 1) if b % i == 0]

        common_factors = [factor for factor in factors_a if factor in factors_b]

        return len(common_factors)