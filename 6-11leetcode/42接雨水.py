# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。
#
#  示例:
#
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#  Related Topics 栈 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        for i,j in enumerate(height):
            while stack and  height[stack[-1]] < j:
                top = stack.pop()
                if not stack:
                    break
                hei = min(height[stack[-1]],j) - height[top]
                dist = i - stack[-1] - 1
                res += hei * dist
            stack.append(i)
        return res


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ds = 0
        h = 0
        while left <= right:
            if height[left] < height[right]:
                if height[left] > h:
                    ds += (height[left] - h) * (right - left + 1)
                    h = height[left]
                left += 1
            else:
                if height[right] > h:
                    ds += (height[right] - h) * (right - left + 1)
                    h = height[right]
                right -= 1
        print(ds,sum(height))
        return ds - sum(height)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    solution = Solution()
    trap = solution.trap([4,2,0,3,2,5])
    print(trap)
