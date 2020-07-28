# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
#  示例 1：
#
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
#  示例 2：
#
#  输入: "cbbd"
# 输出: "bb"
#
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        res = s[0]
        list_ = list(s)
        for i in range(len(s)):
            l = i
            r = i
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if r - l - 1 > len(res):
                res = "".join(list_[l + 1:r])
            l = i
            r = i + 1
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if r - l - 1 > len(res):
                res = "".join(list_[l + 1:r])
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.longestPalindrome("bb")
    print(res)
