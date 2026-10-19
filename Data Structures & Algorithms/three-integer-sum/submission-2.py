class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        i = 0
        for i in range(len(nums)):
            if nums[i]>0:
                return res
            if i>0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                if current_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for the left pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Skip duplicate values for the right pointer
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    r -= 1
                    
        return res

            