class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(base, exp):
            if exp == 0:
                return 1.0
            if exp % 2 == 0:
                return power(base * base, exp // 2)
            else:
                return base * power(base, exp - 1)

        N = n
        if N < 0:
            return 1.0 / power(x, -N)
        return power(x, N)