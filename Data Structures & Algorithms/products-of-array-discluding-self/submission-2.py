class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        total_prod = 1
        res = []
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                total_prod *= num


        if zeros>1:
            return [0] * len(nums)

        for num in nums:
            if zeros == 1 and num == 0:
                res.append(int(total_prod))
            elif zeros == 1:
                res.append(0)
            else:
                res.append(int(total_prod/num))

        return res