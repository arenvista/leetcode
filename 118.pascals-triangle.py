# @leet start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle: List[List[int]] = []

        if numRows == 0:
            return triangle

        first_row: List[int] = [1]
        triangle.append(first_row)

        for i in range(1, numRows):
            row_prev = triangle[i-1]
            row_curr = [1] #we know we always start and end with 1; covers the 1st

            j = 1
            while j < i:
                row_curr.append(row_prev[j-1] + row_prev[j])
                j += 1
            
            row_curr.append(1) #adding the final 1
            triangle.append(row_curr)
        return triangle
# @leet end
