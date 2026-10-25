
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(find_first):
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    ans = mid

                    if find_first:
                        right = mid - 1  # Search left
                    else:
                        left = mid + 1   # Search right

                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        first = binary_search(True)

        if first == -1:
            return [-1, -1]

        last = binary_search(False)

        return [first, last]
