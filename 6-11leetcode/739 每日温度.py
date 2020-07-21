# 根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
#
#  例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2
# , 1, 1, 0, 0]。
#
#  提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
#  Related Topics 栈 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dailyTemperatures(self, T):
        """
        超级垃圾的暴力法
        :type T: List[int]
        :rtype: List[int]
        """
        # length = len(T)
        # if length <= 1:
        #     return []
        # res = []
        # for i in range(length):
        #     for j in range(i+1,length):
        #         if T[j] > T[i]:
        #             res.append(j-i)
        #             break
        #     else:
        #         res.append(0)
        # return res

        # stack = []
        # length = len(T)
        # res = [0] * length
        # for i in range(len(T)):
        #     if not stack or T[stack[-1]] > T[i]:
        #         stack.append(i)
        #     else:
        #         while stack and T[i] > T[stack[-1]]:
        #             index = stack.pop(-1)
        #             res[index] = i - index
        #         stack.append(i)
        # return res

        stack = []
        res = [0] * len(T)
        for i,j in enumerate(T):
            while stack and j > T[stack[-1]]:
                # pop默认弹出最后一个元素，如果需要弹出最后一个元素，就不要写pop(-1)因为很慢超级慢
                res[stack.pop()] = i - stack[-1]
            stack.append(i)
        return res





# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # solution = Solution()
    # res = solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    # print(res)
    l = [1, 2, 3, 4]
    print(l.pop())



