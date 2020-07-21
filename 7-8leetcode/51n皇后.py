# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
#  上图为 8 皇后问题的一种解法。
#
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#  示例:
#
#  输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#
#
#
#
#  提示：
#
#
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步
# ，可进可退。（引用自 百度百科 - 皇后 ）
#
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def dfs(queens,xy_diff,xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    dfs(queens+[q],xy_diff+[p-q],xy_sum+[p+q])

        result = []
        print(result)
        dfs([],[],[])
        return [["."*j+"Q"+"."*(n-j-1) for j in i] for i in result ]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    n_queens = solution.solveNQueens(4)
    print(n_queens)
