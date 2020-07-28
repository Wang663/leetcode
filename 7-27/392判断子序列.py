# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#
#  你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
#
#  字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"ae
# c"不是）。
#
#  示例 1:
# s = "abc", t = "ahbgdc"
#
#  返回 true.
#
#  示例 2:
# s = "axc", t = "ahbgdc"
#
#  返回 false.
#
#  后续挑战 :
#
#  如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码
# ？
#
#  致谢:
#
#  特别感谢 @pbrother 添加此问题并且创建所有测试用例。
#  Related Topics 贪心算法 二分查找 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[j+1][i+1] = dp[j][i] + 1
                else:
                    dp[j + 1][i + 1] = max(dp[j][i+1],dp[j+1][i])
                if dp[j + 1][i + 1] == len(s):
                    return True
        return dp[-1][-1] == len(s)

    def isSubsequence(self,s,t):
        p = q = 0
        while (p < len(s) and q < len(t)):
            if s[p] == t[q]:
                p += 1
            q += 1
        return p == len(s)


if __name__ == '__main__':
    solution = Solution()
    s = "abc"
    t = "abcd"
    res = solution.isSubsequence(s, t)
    print(res)


# leetcode submit region end(Prohibit modification and deletion)
