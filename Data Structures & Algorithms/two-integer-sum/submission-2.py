class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cd = {}

        for i,num in enumerate(nums):
            complement  = target - num
            if complement in cd:
                return [cd[complement], i]

            cd[num] = i

        return []