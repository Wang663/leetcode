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


# dp = do[now] + dp[now-2]

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0

        stack = []
        ans = 0
        for i in range(len(s)):
            # 入栈条件
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)     # 下标入栈
            else:
                # 计算结果
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans




if __name__ == '__main__':
    solution = Solution()
    res = solution.longestValidParentheses("()(())")
    print(res)

# leetcode submit region end(Prohibit modification and deletion)
