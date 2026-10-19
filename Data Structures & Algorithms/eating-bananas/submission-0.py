import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_left = 1
        k_right = max(piles)
        result = k_right
        while k_left <= k_right:
            k = (k_left + k_right)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                result = min(result,k)
                k_right = k-1

            else:
                k_left = k+1


    
        return result