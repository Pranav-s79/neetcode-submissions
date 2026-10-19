class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod,zeros = 1,0

        for num in nums:
            if num != 0:
                total_prod *= num
            else:
                zeros+=1

            #gets total product iwthout including 0 in product

        if zeros >1 : return [0]*len(nums)
        res = []
        for num in nums:
            if num == 0:
                res.append(int(total_prod))
            elif zeros == 1:
                res.append(0)
            else:
                res.append(int(total_prod/num))

        return res
