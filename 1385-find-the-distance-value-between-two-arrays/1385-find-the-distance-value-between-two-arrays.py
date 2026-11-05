class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = sorted(arr2) + [inf]  # sentinel: the pointer never runs off the end
        j = 0

        def far(a):  # a only grows, so the first b >= a - d only moves right
            nonlocal j
            while arr2[j] < a - d:
                j += 1
            return arr2[j] > a + d

        return sum(map(far, sorted(arr1)))