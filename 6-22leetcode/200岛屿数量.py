# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1:
#
#  输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
#
#
#  示例 2:
#
#  输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i, j in enumerate(grid):
            for x, z in enumerate(j):
                if z == "1":
                    res += 1
                    self.dfs(grid, i, x)
        return res

    def dfs(self, grid, i, x):
        length1 = len(grid)
        length2 = len(grid[0])
        step = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        quene = collections.deque()
        quene.append((i, x))
        while quene:
            i, x = quene.popleft()
            if 0 <= i <= length1 and 0 <= x <= length2 and grid[i][x] == "1":
                grid[i][x] = "0"
                for w,z in step:
                    quene.append((w+i,x+z))

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    solution.numIslands()
