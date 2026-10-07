class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        flat = m*n
        l = 0 
        r = flat-1

        while l <= r:
            m = (l+r)//2
            row = m // n
            col = m % n
            if target > matrix[row][col]:
                l = m+1
            elif target < matrix[row][col]:
                r = m-1
            else:
                return True 
        return False




            