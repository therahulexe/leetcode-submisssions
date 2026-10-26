class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            visited.add((r, c))
            total = grid[r][c]

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n
                    and grid[nr][nc] > 0
                    and (nr, nc) not in visited):
                    total += dfs(nr, nc)

            return total

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and (i, j) not in visited:
                    island_sum = dfs(i, j)

                    if island_sum % k == 0:
                        count += 1

        return count