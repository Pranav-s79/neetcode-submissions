class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}

        for i,num in enumerate(nums):
            if num in m:
                return True

            m[num] = 1

        return False
