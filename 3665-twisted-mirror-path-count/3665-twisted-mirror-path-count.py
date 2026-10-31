class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        right = [0] * n
        down = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    right[0] = 1
                    down[0] = 0
                    continue
                from_top = 0
                if i > 0:
                    if grid[i - 1][j] == 0:
                        from_top = (right[j] + down[j]) % MOD
                    else:
                        from_top = right[j]
                from_left = 0
                if j > 0:
                    if grid[i][j - 1] == 0:
                        from_left = (right[j - 1] + down[j - 1]) % MOD
                    else:
                        from_left = down[j - 1]
                down[j] = from_top
                right[j] = from_left

        return (right[n - 1] + down[n - 1]) % MOD