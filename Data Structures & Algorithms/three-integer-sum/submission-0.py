
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        f = {}
        nums.sort()

        for i,num in enumerate(nums):
            j= i+1
            k = len(nums) -1

            while j<k:
                tot = nums[i] + nums[j]+nums[k]

                if tot>0:
                    k-=1
                elif tot<0:
                    j+=1
                elif tot == 0:
                    if (nums[i], nums[j],nums[k]) not in f:
                        f[(nums[i], nums[j],nums[k])] = 1
                    k-=1
                    j+=1

        return [list(i) for i in f.keys()]