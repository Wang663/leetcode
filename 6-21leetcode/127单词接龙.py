# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#
#
#
#  每次转换只能改变一个字母。
#  转换过程中的中间单词必须是字典中的单词。
#
#
#  说明:
#
#
#  如果不存在这样的转换序列，返回 0。
#  所有单词具有相同的长度。
#  所有单词只由小写字母组成。
#  字典中不存在重复的单词。
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
#
#  示例 1:
#
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5
#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#
#
#  示例 2:
#
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: 0
#
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
#  Related Topics 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # word_set = set(wordList)
        # if len(word_set) == 0 or endWord not in word_set:
        #     return 0
        #
        # if beginWord in word_set:
        #     word_set.remove(beginWord)
        #
        # queue = deque()
        # queue.append(beginWord)
        #
        # visited = set()
        # visited.add(beginWord)
        #
        # word_len = len(beginWord)
        # step = 1
        #
        # while queue:
        #     current_size = len(queue)
        #     for i in range(current_size):
        #         word = queue.popleft()
        #
        #         word_list = list(word)
        #         for j in range(word_len):
        #             origin_char = word_list[j]
        #
        #             for k in range(26):
        #                 word_list[j] = chr(ord('a') + k)
        #                 next_word = ''.join(word_list)
        #                 if next_word in word_set:
        #                     if next_word == endWord:
        #                         return step + 1
        #                     if next_word not in visited:
        #                         queue.append(next_word)
        #                         visited.add(next_word)
        #             word_list[j] = origin_char
        #     step += 1
        # return 0


        # =================bfs
        # dict_ = {i:1 for i in wordList}
        #
        # if beginWord in dict_:
        #     dict_.pop(beginWord)
        #
        # if len(beginWord) != len(endWord):
        #     return -1
        #
        # if endWord not in dict_:
        #     return -1
        #
        # visited = set()
        # res = 0
        # def bfs():
        #     nonlocal res
        #     quene = [(beginWord,1)]
        #
        #     while quene:
        #         elem, num = quene.pop(0)
        #         if elem == endWord:
        #             res = num
        #             return
        #         for i, j in enumerate(elem):
        #             for w in range(26):
        #                 char = chr(ord("a") + w)
        #                 if char != j:
        #                     tmp = elem[:i] + char + elem[i + 1:]
        #                     if tmp in dict_ and tmp not in visited:
        #                         quene.append((tmp, num + 1))
        #                         visited.add(tmp)
        #
        # bfs()
        # return res


# dfs
        dict_ = {i:1 for i in wordList}
        max_num = len(dict_)




        if len(beginWord) != len(endWord):
            return 0

        if endWord not in dict_:
            return 0

        def dfs(current, num,dict_bank):
            nonlocal max_num
            # terminator
            if num > max_num:
                return
            if current == endWord:
                if num < max_num:
                    max_num = num
                return
            if not dict_bank:
                return

            for i, j in enumerate(current):
                for w in range(26):
                    char = chr(ord("a") + w)
                    tmp = current[:i] + char + current[i + 1:]
                    if tmp in dict_bank:
                        dict_bank.pop(tmp)
                        # drill down
                        dfs(tmp,num+1,dict_bank)
                        # reverse state
                        dict_bank[tmp] = 1

        dfs(beginWord, 0,dict_)

        return max_num if max_num <= len(dict_) else -1


class Solution:

    """
    双向BFS
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # for O(1) time complexity
        begin_set, end_set, visited_words, words = set(), set(), set(), set(wordList)

        if endWord not in words:
            return 0

        ladder_len = 1

        begin_set.add(beginWord)
        end_set.add(endWord)
        alphabet = list('abcdefghijklmnopqrstuvwxyz')

        while begin_set and end_set:
            # two-end BFS
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            candidate_begin = []
            for word in begin_set:
                word_to_list = list(word)
                for i in range(len(word_to_list)):
                    old_ch = word_to_list[i]
                    for ch in alphabet:
                        word_to_list[i] = ch
                        new_word = ''.join(word_to_list)
                        if new_word in end_set:
                            return ladder_len + 1
                        if new_word not in visited_words and new_word in words:
                            candidate_begin.append(new_word)
                            visited_words.add(new_word)
                    word_to_list[i] = old_ch

            begin_set = set(candidate_begin)
            ladder_len += 1

        return 0

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.ladderLength("hot", "dog", ["hot","hoo","hod", "dog"])
    print(res)
    a = []
