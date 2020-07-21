# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#
#  每行中的整数从左到右按升序排列。
#  每行的第一个整数大于前一行的最后一个整数。
#
#
#  示例 1:
#
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#
#
#  示例 2:
#
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # if not matrix or len(matrix[0]) == 0:
        #     return False
        # x, y = 0, 0
        # while True:
        #     if matrix[x][y] == target:
        #         return True
        #     elif x+1 < len(matrix) and matrix[x+1][y] <= target:
        #         x = x+1
        #     else:
        #         for i in matrix[x]:
        #                     if i == target:
        #                         return True
        #                     elif i > target:
        #                         return False
        #                 break
        # return False

        if not matrix or len(matrix[0]) == 0:
            return False
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        length = len(matrix[0])
        while l <= r:
            mid = (l + r) // 2
            row = mid // length
            line = mid % length
            if matrix[row][line] == target:
                return True
            elif matrix[row][line] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    matrix = [[1]]
    target = 3
    res = solution.searchMatrix(matrix, target)
    print(res)
