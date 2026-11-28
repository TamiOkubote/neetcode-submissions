from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                box_key = (r // 3, c // 3)
                if value == ".":
                    continue
                if (value in row[r]) or (value in column[c]) or (value in box[box_key]):
                    return False
                row[r].add(value)
                column[c].add(value)
                box[box_key].add(value)        
        return True