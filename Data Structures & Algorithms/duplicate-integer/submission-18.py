class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s  = {}       
        for num in nums:
            if num in s:
                return True
            s[num] = s.get(num, 0) + 1


        return False

