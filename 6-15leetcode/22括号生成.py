# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例：
#
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = ["()"]
        if n ==1:
            return res
        res = self.generateParenthesis(n-1)
        temp_res = []
        for i in res:
            for j in range(len(i)):
                temp_res.append(i[:j]+"()"+i[j:])
        return list(set(temp_res))
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.generateParenthesis(4)
    print(res)
    print(len(res))


# i = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
# j = ['()(()())', '()()(())', '(()(()))', '(((())))', '(()())()', '((())())', '()(())()', '()((()))', '()()()()', '(())()()', '((()()))', '((()))()', '(()()())']
# print(len(i))
# print(len(j))
# for w in i:
#     if w not in j:
#         print(w)