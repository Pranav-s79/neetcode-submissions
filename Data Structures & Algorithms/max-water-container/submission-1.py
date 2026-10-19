class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #height = heights[i]
        #width = difference  in i
        l,r = 0, len(heights) -1 
        maxim = min(heights[l],heights[r]) * (r-l)

        while l<r:
            curr = min(heights[l], heights[r]) * (r-l)
            maxim = max(maxim,curr)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1


        return maxim

            