# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
#
#
#  示例 1:
#
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
#  示例 2:
#
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
import copy

from typing import List

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_elem = [nums[0]]
        min_elem = [nums[0]]
        for i in nums[1:]:
            tmp = (max_elem[-1] * i, min_elem[-1] * i, i)
            max_elem.append(max(tmp))
            min_elem.append(min(tmp))
        return max(max_elem)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1 # or 1的作用是，当nums[i - 1]==0时，nums[i]乘等自身
            nums_reverse[i] *= nums_reverse[i - 1] or 1
        return max(max(nums),max(nums_reverse))


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.maxProduct([-2, 0, -1])
    print(res)
    print((0 or 1))
