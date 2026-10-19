class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if not nums:
            return 0

        max_conseq = 1
        curr_conseq = 1
        left,right = 0,1
        while right<len(nums):
            if nums[right-1]+1 == nums[right]:
                curr_conseq += 1
                right +=1
            else:
                left = right
                right +=1
                curr_conseq =1 
            if curr_conseq >max_conseq:
                max_conseq = curr_conseq


        return max_conseq

