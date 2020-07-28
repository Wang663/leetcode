# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
#
#
#
#
#
#
#  示例 1：
#
#  输入："ab-cd"
# 输出："dc-ba"
#
#
#  示例 2：
#
#  输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#
#
#  示例 3：
#
#  输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#
#
#
#
#  提示：
#
#
#  S.length <= 100
#  33 <= S[i].ASCIIcode <= 122
#  S 中不包含 \ or "
#
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        list_ = [i for i in S if "a" <= i <= "z" or "A" <= i <= "Z"]
        res = []
        for i in range(len(S)):
            if "a" <= S[i] <= "z" or "A" <= S[i] <= "Z":
                res.append(list_.pop())
            else:
                res.append(S[i])
        return "".join(res)



# leetcode submit region end(Prohibit modification and deletion)
