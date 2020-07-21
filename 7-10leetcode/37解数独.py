# 编写一个程序，通过已填充的空格来解决数独问题。
#
#  一个数独的解法需遵循如下规则：
#
#
#  数字 1-9 在每一行只能出现一次。
#  数字 1-9 在每一列只能出现一次。
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#
#
#  空白格用 '.' 表示。
#
#
#
#  一个数独。
#
#
#
#  答案被标成红色。
#
#  Note:
#
#
#  给定的数独序列只包含数字 1-9 和字符 '.' 。
#  你可以假设给定的数独只有唯一解。
#  给定数独永远是 9x9 形式的。
#
#  Related Topics 哈希表 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
import copy
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.row = [set() for _ in range(9)]
        self.column = [set() for _ in range(9)]
        self.block = [set() for _ in range(9)]
        self.board = board
        self.res = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                elem = board[i][j]
                if elem != ".":
                    block_num = (i // 3) * 3 + (j // 3)
                    row_num = i
                    column_num = j
                    self.block[block_num].add(elem)
                    self.row[row_num].add(elem)
                    self.column[column_num].add(elem)
        self.dfs(0, 0)
        return self.board


    def dfs(self, i, j):
        if i >= len(self.board):
            self.res = copy.deepcopy(self.board)
            return True
        if self.board[i][j] != ".":
            self.dfs(i + (j+1) // 9, (j+1) % 9)
        else:
            for w in range(1, 10):
                block_num = (i // 3) * 3 + (j // 3)
                row_num = i
                column_num = j
                elem = str(w)
                if elem not in self.block[block_num] and elem not in self.row[row_num] and elem not in self.column[column_num]:
                    self.board[i][j] = elem
                    self.block[block_num].add(elem)
                    self.row[row_num].add(elem)
                    self.column[column_num].add(elem)
                    dfs_res = self.dfs(i + (j + 1) // 9, (j + 1) % 9)
                    self.board[i][j] = "."
                    self.block[block_num].remove(elem)
                    self.row[row_num].remove(elem)
                    self.column[column_num].remove(elem)


if __name__ == '__main__':
    solution = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    board = solution.solveSudoku(board)
    print(board)

# leetcode submit region end(Prohibit modification and deletion)
