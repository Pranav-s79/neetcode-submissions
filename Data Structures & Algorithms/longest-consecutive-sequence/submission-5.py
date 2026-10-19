class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        if not nums:
            return 0
        max_c = 1
        curr = 1
        #[0,1,2,3,4,5,6]
        l,r = 0,1
        while r<len(nums):
            if nums[r-1] + 1 == nums[r]:
                curr +=1
                r += 1
            else:
                l = r
                r+=1
                curr = 1

            max_c = max(max_c,curr) 


        return max_c