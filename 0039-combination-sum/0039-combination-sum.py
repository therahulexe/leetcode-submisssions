
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    continue

                path.append(num)
                backtrack(i, remaining - num)  # Reuse same number
                path.pop()                     # Backtrack

        candidates.sort()
        backtrack(0, target)

        return result
