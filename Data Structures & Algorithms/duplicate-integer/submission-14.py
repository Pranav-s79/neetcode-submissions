class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for i in nums:
            if i not in dictionary:
                dictionary[i] = i

            else :
                return True

        return False            