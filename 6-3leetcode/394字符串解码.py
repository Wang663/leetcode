# 给定一个经过编码的字符串，返回它解码后的字符串。
#
#  编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
#  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
#  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
#  示例:
#
#
# s = "3[a]2[bc]", 返回 "aaabcbc".
# s = "3[a2[c]]", 返回 "accaccacc".
# s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
#
#  Related Topics 栈 深度优先搜索


# 6-3leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    # def decodeString(self, s: str) -> str:
    #     stack, res, multi = [], "", 0
    #     for c in s:
    #         if c == '[':
    #             stack.append([multi, res])
    #             res, multi = "", 0
    #         elif c == ']':
    #             cur_multi, last_res = stack.pop()
    #             res = last_res + cur_multi * res
    #         elif '0' <= c <= '9':
    #             multi = multi * 10 + int(c)
    #         else:
    #             res += c
    #     return res
    def decodeString(self, s: str) -> str:
        stack = []
        num = ""
        res = ""
        for i in s:
            if i == "[":
                stack.append([int(num),res])
                num = ""
                res = ""
            elif i >= "0" and i <= "9":
                num+=i
            elif i == "]":
                temp_num,current_res = stack.pop(-1)
                res = current_res+temp_num*res
            else:
                res+=i
        return res




# 6-3leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    two_sum = solution.decodeString("3[a2[c]]")
    print(two_sum)
