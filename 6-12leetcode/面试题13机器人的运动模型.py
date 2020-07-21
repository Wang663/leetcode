# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一
# 格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但
# 它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
#
#
#  示例 1：
#
#  输入：m = 2, n = 3, k = 1
# 输出：3
#
#
#  示例 2：
#
#  输入：m = 3, n = 1, k = 0
# 输出：1
#
#
#  提示：
#
#
#  1 <= n,m <= 100
#  0 <= k <= 20
#
#


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution(object):
#     def movingCount(self, m, n, k):
#         """
#         :type m: int
#         :type n: int
#         :type k: int
#         :rtype: int
#         """
#
#         """
#         广度优先遍历
#         """
#         quene = [(0, 0, 0, 0)]
#         visited = set()
#         while quene:
#             i, j, si, sj = quene.pop(0)
#             if i >= m or j >= n or si + sj > k or (i, j) in visited:
#                 continue
#             visited.add((i, j))
#             quene.append((i + 1, j, si + 1 if (i + 1) % 10 != 0 else si - 8, sj))
#             quene.append((i, j + 1, si, sj + 1 if (j + 1) % 10 != 0 else sj - 8))
#             print(quene)
#         return len(visited)


class Solution(object):
    def movingCount(self, m, n, k):
        """
        深度优先遍历
        :param m:
        :param n:
        :param k:
        :return:
        """
        visited = set()
        def dfs(i,j,si,sj):
            if i >= m or j>= n or si + sj > k or (i,j) in visited:
                return 0
            visited.add((i,j))
            return 1+dfs(i + 1, j, si + 1 if (i + 1) % 10 != 0 else si - 8, sj)+dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 != 0 else sj - 8)

        return dfs(0,0,0,0)



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    count = solution.movingCount(3, 2, 17)
    print(count)
