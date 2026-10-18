class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        # Calculate combinations: C(n, k)
        def comb(n, k):
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            ways = comb(len(left) + len(right), len(left))
            ways = ways * dfs(left) % MOD
            ways = ways * dfs(right) % MOD

            return ways

        return (dfs(nums) - 1) % MOD