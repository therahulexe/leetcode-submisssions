class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        n = len(nums)
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                curr = nums[i]+nums[l]+nums[r]
                if abs(res-target) > abs(curr-target):
                    res = curr
                if curr==target:
                    return curr
                elif curr>target:
                    r-=1
                else:
                    l+=1
        return res

                    