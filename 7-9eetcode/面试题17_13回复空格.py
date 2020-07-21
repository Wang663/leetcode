# 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’
# t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一
# 本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。
#
#
#  注意：本题相对原题稍作改动，只需返回未识别的字符数
#
#
#
#  示例：
#
#  输入：
# dictionary = ["looked","just","like","her","brother"]
# sentence = "jesslookedjustliketimherbrother"
# 输出： 7
# 解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
#
#
#  提示：
#
#
#  0 <= len(sentence) <= 1000
#  dictionary中总字符数不超过 150000。
#  你可以认为dictionary和sentence中只包含小写字母。
#
#  Related Topics 记忆化 字符串


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        trie = Trie(dictionary)
        print(trie.dict_)
        dp = [0 for i in range(len(sentence)+1)]
        for i in range(1,len(sentence)+1):
            dp[i] = dp[i-1] + 1
            search_res = trie.search(i, sentence)

            for j in search_res:
                dp[i] = min(dp[i],dp[j])
        return dp[-1]



class Trie():

    def __init__(self,dictionary):
        self.dict_ = self.get_dictionary(dictionary)


    def get_dictionary(self,dictionary):
        dict_ = {}
        for i in dictionary:
            tmp = dict_
            for char in i[::-1]:
                tmp.setdefault(char, {})
                tmp = tmp[char]
            tmp["end"] = True
        return dict_

    def search(self,endpos,sentence):
        tmp = self.dict_
        res = []
        for i in range(endpos-1,-1,-1):
            if sentence[i] in tmp:
                tmp = tmp[sentence[i]]
                if "end" in tmp:
                    print("======")
                    print(i)
                    res.append(i)
            else:
                break
        return res



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    dictionary = ["looked","just","like","her","brother"]
    sentence = "jesslookedjustliketimherbrother"
    respace = solution.respace(dictionary, sentence)
    print(respace)
