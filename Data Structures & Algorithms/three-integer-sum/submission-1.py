class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        f = {}
        for i, num in enumerate(nums):
            l = i+1
            r = len(nums) - 1

            while l<r:
                tot = num+nums[l]+nums[r]
                if tot>0:
                    r-=1
                elif tot<0:
                    l+=1

                elif tot == 0:
                    key = (num, nums[l],nums[r])
                    if key not in f:
                        f[key] = 1
                    l+=1
                    r-=1

        return [list(k) for k in f]
        