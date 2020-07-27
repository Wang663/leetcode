# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#  示例:
#
#  输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6
#  Related Topics 栈 数组 哈希表 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List



class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        可以将本题理解为84题，然后使用单调栈来解决
        """
        def fun(list_:List):
            res = 0
            stack = [-1]
            for i in range(len(list_)):
                while stack[-1] != -1 and list_[i] < list_[stack[-1]]:
                    res = max(res,list_[stack.pop()] * ((i-stack[-1])-1))
                stack.append(i)
            length = len(list_)
            for i in stack[::-1]:
                if i == -1:
                    continue
                res =max(res,list_[stack.pop()] * ((length-stack[-1])-1))
            return res


        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        length = len(matrix[0])
        elem =[0 for _ in range(length)]
        res = 0
        for i in matrix:
            for j in range(length):
                if i[j] == "1":
                    elem[j] = elem[j] + 1
                else:
                    elem[j] = 0
            res = max(res,fun(elem))
        return res




# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    # matrix = [["1","1"]]
    solution = Solution()
    res = solution.maximalRectangle(matrix)
    print(res)
