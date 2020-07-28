# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
#  你可以对一个单词进行如下三种操作：
#
#
#  插入一个字符
#  删除一个字符
#  替换一个字符
#
#
#
#
#  示例 1：
#
#  输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
#  示例 2：
#
#  输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        for i in range(len(word2)+1):
            dp[i][0] = i
        for i in range(len(word1) + 1):
            dp[0][i] = i
        for i in range(len(word2)):
            for j in range(len(word1)):
                left = dp[i][j+1] + 1
                down = dp[i+1][j] + 1
                left_down = dp[i][j]
                if word2[i] != word1[j]:
                    left_down += 1
                dp[i+1][j+1] = min(left, down, left_down)
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    word1 = "horse"
    word2 = "ros"
    res = solution.minDistance(word1, word2)
    print(res)
