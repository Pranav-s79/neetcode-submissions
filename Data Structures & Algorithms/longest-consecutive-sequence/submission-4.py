class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0

        for num in nums:
            if (num - 1) not in s:
                curr_num = num
                length = 1

                while(curr_num + 1) in s:
                    length +=1
                    curr_num +=1
                

                max_len = max(length,max_len)

        return max_len

