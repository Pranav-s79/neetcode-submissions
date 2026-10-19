class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product,zero= 1,0
        for num in nums:
            if num == 0:
                zero+=1
            else:
                total_product *= num


            if zero>1: return [0]*len(nums)

        output = []
        for num in nums:
            if zero == 1:
                # only the zero position gets the product
                if num == 0:
                    output.append(total_product)
                else:
                    output.append(0)
            else:
                # no zeros case
                output.append(total_product // num)

        return output