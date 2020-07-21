# 在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。
#
#  一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：
#
#
#  相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
#  C_1 位于 (0, 0)（即，值为 grid[0][0]）
#  C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
#  如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
#
#
#  返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。
#
#
#
#  示例 1：
#
#  输入：[[0,1],[1,0]]
#
# 输出：2
#
#
#
#  示例 2：
#
#  输入：[[0,0,0],[1,1,0],[1,1,0]]
#
# 输出：4
#
#
#
#
#
#  提示：
#
#
#  1 <= grid.length == grid[0].length <= 100
#  grid[i][j] 为 0 或 1
#
#  Related Topics 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from queue import PriorityQueue


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        length = len(grid)
        viseted,begin_visited,end_visited = set(),set(),set()
        begin_visited.add((0,0))
        end_visited.add((length-1, length-1))
        viseted.add((0,0))
        viseted.add((length-1, length-1))
        res = 2
        step = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        while begin_visited and end_visited:
            if len(begin_visited)> len(end_visited):
                begin_visited,end_visited = end_visited,begin_visited
            tmp_visited = set()
            for row,column in begin_visited:
                for i,j in step:
                    if 0 <= row+i <= length-1 and 0 <= column+j <= length-1 and grid[row+i][column+j]==0:
                        if (row+i, column+j) in end_visited:
                            return res
                        if (row+i, column+j) not in viseted:
                            tmp_visited.add((row+i, column+j))
                            viseted.add((row+i, column+j))
            res += 1
            begin_visited = tmp_visited
        return -1

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    res = solution.shortestPathBinaryMatrix(grid)
    print(res)
