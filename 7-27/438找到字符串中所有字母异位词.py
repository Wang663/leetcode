# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
#  说明：
#
#
#  字母异位词指字母相同，但排列不同的字符串。
#  不考虑答案输出的顺序。
#
#
#  示例 1:
#
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#
#
#  示例 2:
#
#
# 输入:
# s: "abab" p: "ab"
#
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#
#  Related Topics 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        def fun(dict_):
            for i, j in dict_.items():
                if j != 0:
                    return False
            return True

        len_p = len(p)
        len_s = len(s)
        if len_s < len_p:
            return []
        tmp = sum([ord(s[i]) for i in range(len_p)])
        target = sum([ord(i) for i in p])
        dict_ = collections.defaultdict(int)
        for i, j in zip(list(p), [s[i] for i in range(len_p)]):
            dict_[i] += 1
            dict_[j] -= 1
        print(dict_)
        res = []
        s_split = list(s)
        if target == tmp and fun(dict_):
            res.append(0)
        for i in range(1,len_s-len_p+1):
            tmp = tmp - ord(s_split[i-1])
            tmp = tmp + ord(s_split[i+len_p-1])
            dict_[s_split[i+len_p-1]] += 1
            dict_[s_split[i-1]] -= 1
            print(dict_)
            if tmp == target and fun(dict_):
                res.append(i)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    s = "baa"
    p = "aa"
    res = solution.findAnagrams(s, p)
    print(res)
