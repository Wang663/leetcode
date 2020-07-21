# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
#
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
#
#  示例:
#
#  输入:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# 输出: ["eat","oath"]
#
#  说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
#
#  提示:
#
#
#  你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
#  如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何
# 实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
#
#  Related Topics 字典树 回溯算法



import collections


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    # def search(self, word):
    #     node = self.root
    #     for w in word:
    #         node = node.children.get(w)
    #         if not node:
    #             return False
    #     return node.isWord

class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            # 将所有的单词插入前缀树中
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 深度优先遍历
                self.dfs(board, node, i, j, "", res)
        print(board)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            # 匹配到字符了
            res.append(path)
            # 标识不再匹配该单词
            node.isWord = False
        #     这个判断写的很好
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        # 获取本单元格的元素
        tmp = board[i][j]
        # 判断是否有这个元素的前缀树
        node = node.children.get(tmp)
        if not node:
            return
        # 标识已经遍历过了
        board[i][j] = "#"
        self.dfs(board, node, i+ 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        # 还原原始元素
        board[i][j] = tmp


if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    solution = Solution()
    res = solution.findWords(board, words)
    print(res)