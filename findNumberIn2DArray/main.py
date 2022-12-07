from typing import List


# --------------------------------------------------------
# 话不多少，先来一波蛮力法压压惊
class Solution:

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for item in matrix:
            for j in range(len(item)):
                if item[j] == target:
                    return True
        return False


# --------------------------------------------------------
# 可以将矩阵想象成为一个二维的坐标轴，左下角作为坐标原点，从原点出发，沿着斜线遍历，斜线上方比此值小，斜线下方比此值大
# 直到行列都超出边界，就退出，说明不存在此元素
class Solution:

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix) - 1, 0
        max_col = len(matrix[0])
        while row >= 0 and col <= max_col -1:
            _v =  matrix[row][col]
            if _v == target:
                return True
            elif _v < target:
                col += 1
            else:
                row -= 1
        return False


if __name__ == "__main__":
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 50
    r = Solution().findNumberIn2DArray(matrix, target)
    print(r)