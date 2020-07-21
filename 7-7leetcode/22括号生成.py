# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例：
#
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []

        self.fun(n, n, "")

        return self.res

    def fun(self, left, right, str):
        if left == 0 and right == 0:
            self.res.append(str)

        if left > 0:
            self.fun(left - 1, right, str + "(")

        if right > left:
            self.fun(left, right - 1, str + ")")

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.generateParenthesis(4)
    print(len(res))
