from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for column in range(9):
                value = board[row][column]
                if value == ".":
                    continue
                box_row = row // 3
                box_column = column // 3
                box_id = (box_row, box_column)
                if (value in rows[row]) or (value in columns[column]) or (value in boxes[box_id]):
                    return False
                rows[row].add(value)
                columns[column].add(value)
                boxes[box_id].add(value)
        return True