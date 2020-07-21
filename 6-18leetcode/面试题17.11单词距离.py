# 有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，
# 你能对此优化吗?
#
#  示例：
#
#  输入：words = ["I","am","a","student","from","a","university","in","a","city"],
# word1 = "a", word2 = "student"
# 输出：1
#
#  提示：
#
#
#  words.length <= 100000
#
#  Related Topics 双指针 字符串


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def findClosest(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dict_ = collections.defaultdict(list)
        for i, j in enumerate(words):
            dict_[j].append(i)

        list1 = dict_[word1]
        list2 = dict_[word2]

        length1 = len(list1)
        length2 = len(list2)

        i, j = 0, 0
        res = float("inf")
        while i < length1 or j < length2:
            if abs(list1[i] - list2[j]) == 1:
                return 1
            res = min(res,abs(list1[i] - list2[j]))
            if list1[i]> list2[j]:
                j +=1
            else:
                i +=1
        return res

    def findClosest(self, words, word1, word2):
        i, j = None, None
        res = float("inf")
        for index,elem in enumerate(words):
            if elem == word1:
                i = index
                if i and j:
                    res = min(res,abs(i-j))
            elif elem == word2:
                j = index
                if i and j:
                    res = min(res,abs(i-j))
        return res





# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    distance = solution.findClosest(["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"], "a",
                                   "student")
    print(distance)
