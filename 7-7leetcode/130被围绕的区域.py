# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
#  找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
#  示例:
#
#  X X X X
# X O O X
# X X O X
# X O X X
#
#
#  运行你的函数后，矩阵变为：
#
#  X X X X
# X X X X
# X X X X
# X O X X
#
#
#  解释:
#
#  被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被
# 填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        step = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i, j):
            for step_y, step_x in step:
                if 0 <= step_y + i < len(board) and 0 <= step_x + j < len(board[0]) and board[step_y+ i][step_x+ j] == "O":
                    board[step_y+ i][step_x+ j] = "A"
                    dfs(step_y + i,step_x + j)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1) and board[i][j] == "O":
                    board[i][j] = "A"
                    dfs(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"

# leetcode submit region end(Prohibit modification and deletion)
