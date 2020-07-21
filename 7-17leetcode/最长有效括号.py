# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
#  示例 1:
#
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#
#
#  示例 2:
#
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        for i in range(len(s)):
            if s[i] == ")" and stack and s[stack[-1]] == "(":
                stack.pop()
                res = max(res,i - (stack[-1] if stack else -1))
            else:
                stack.append(i)

        return res


class Solution(object):
    def longestValidParentheses(self, s):
        if len(s) <= 1:
            return 0
        dp = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] == ")":
                if i-1 >= 0 and s[i-1] == "(":
                    dp[i] = (dp[i-2] if i-2 >=0 else 0)+2
                elif s[i-1] == ")":
                    if dp[i-1] > 0 and i - dp[i-1]-1 >= 0 and s[i - dp[i-1]-1] == "(":
                        dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1]-2] if i - dp[i-1]-2 >0 else 0)
        print(dp)
        return max(dp)






# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.longestValidParentheses("(()())")
    print(res)



