class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        top, bot = 0, m-1

        while top<=bot:
            mid_r = (bot+top)//2
            if matrix[mid_r][0] <= target <= matrix[mid_r][-1]:
                break
            elif matrix[mid_r][0]>target:
                bot = mid_r -1
            elif matrix[mid_r][0]<target:
                top = mid_r +1

        if top> bot:
            return False

        l,r = 0, n-1
        while l<=r:
            mid_c = (l+r)//2
            if matrix[mid_r][mid_c] == target:
                return True
            elif matrix[mid_r][mid_c]<target:
                l = mid_c + 1
            else:
                r = mid_c -1

        return False

