# @leet start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]


        for row_ind in range(N):
            for col_ind in range(N):
                val = board[row_ind][col_ind]
                if val == ".":
                    continue
                # Validate Rows
                if val in rows[row_ind]:
                    return False

                rows[row_ind].add(val)

                # Validate Cols

                if val in cols[col_ind]:
                    return False 

                cols[col_ind].add(val)

                # Validate Boxes
                idx = (row_ind // 3 ) * 3 + col_ind // 3 
                if  val in boxes[idx]:
                    return False

                boxes[idx].add(val)

        return True


# @leet end
