# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
#  示例:
#
#  输入: [2,1,5,6,2,3]
# 输出: 10
#  Related Topics 栈 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return None
        res = heights[0]
        stack = [-1]
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                res = max(res,heights[stack.pop(-1)]*(i-stack[-1]-1))
            stack.append(i)
            print(stack)
            print(res)
        length = len(heights)

        for i in stack[::-1]:
            if i==-1:
                continue
            res = max(res,heights[stack.pop(-1)]*(length-stack[-1]-1))
        return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # solution = Solution()
    # res = solution.largestRectangleArea([2, 1, 5, 6, 2, 3])
    # print(res)
    i = reversed([1, 2, 3])
    l = list(123)



