# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
#
#
#
#  示例 1：
#
#  输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#
#
#
#
#  提示：
#
#
#  S的长度在[1, 500]之间。
#  S只包含小写字母 'a' 到 'z' 。
#
#  Related Topics 贪心算法 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def partitionLabels(self, S):
        """
        当前区间的范围必包含当前元素的随后的位置，依次遍历区间的元素，获取区间元素最后的位置
        用于更新区间长度。
        :type S: str
        :rtype: List[int]
        """
        dict_ = {j: i for i, j in enumerate(S)}
        start, end = 0, 0
        res = []
        for i, j in enumerate(S):
            end = max(end,dict_[j])
            if end == i:
                res.append(end - start +1)
                start = end + 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    labels = solution.partitionLabels("ababcbacadefegdehijhklij")
    print(labels)
