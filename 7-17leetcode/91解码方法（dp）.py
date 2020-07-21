# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
#  示例 1:
#
#  输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#
#
#  示例 2:
#
#  输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]
        if s[0] == '0':
            return 0
        dp[0] = 1
        for i in range(1, size):
            if s[i] != '0':
                # 把这一位数字当做单独字符来处理，如果是0就没法单做单独字符
                dp[i] = dp[i - 1]
            # 取出这一位和前一位所组成的数字
            num = int("".join(s[i-1:i+1]))

            if 10 <= num <= 26:
                # 特殊处理
                if i == 1:
                    dp[i] += 1
                else:
                    # 可以理解为斐波拉切数列
                    dp[i] += dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    solution.numDecodings("2261")
