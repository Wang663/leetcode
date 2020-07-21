# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
#  示例:
#
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
#  说明：
#
#
#  所有输入均为小写字母。
#  不考虑答案输出的顺序。
#
#  Related Topics 哈希表 字符串


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_ = collections.defaultdict(list)
        for i in range(len(strs)):
            dict_[tuple(sorted(strs[i]))].append(strs[i])
        return dict_.values()


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution.groupAnagrams(strs)





