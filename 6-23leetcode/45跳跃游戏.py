# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
#  示例:
#
#  输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
#  说明:
#
#  假设你总是可以到达数组的最后一个位置。
#  Related Topics 贪心算法 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        # maxPos 最远能达到的距离
        # end 本次最远能达到的值
        # step 步数
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
            print(maxPos, end, step)
        return step








class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        maxpos = 0
        end = 0
        for i in range(len(nums)-1):
            if maxpos >= i:
                maxpos = max(maxpos,nums[i]+i)
                if i == end:
                    end = maxpos
                    step += 1
        return step




if __name__ == '__main__':
    solution = Solution()
    res = solution.jump([2, 3, 1, 1, 4])
    print(res)

# leetcode submit region end(Prohibit modification and deletion)
