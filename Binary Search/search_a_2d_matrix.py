import math


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break

        if not (top <= bot):
            return False

        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            col = (l + r) // 2
            if matrix[row][col] > target:
                r = col - 1
            elif matrix[row][col] < target:
                l = col + 1
            else:
                return True

        return False

