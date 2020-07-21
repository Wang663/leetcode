# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
#
#  返回滑动窗口中的最大值。
#
#
#
#  进阶：
#
#  你能在线性时间复杂度内解决此题吗？
#
#
#
#  示例:
#
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^5
#  -10^4 <= nums[i] <= 10^4
#  1 <= k <= nums.length
#
#  Related Topics 堆 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # data = nums[:k]
        # max_stack = [max(data)]
        # res = [max_stack[0]]
        # for i in nums[k:]:
        #     if i >= max_stack[0]:
        #         max_stack.pop(0)
        #         max_stack.append(i)
        #     head = data.pop(0)
        #     data.append(i)
        #     if head == max_stack[0]:
        #         max_stack.pop(0)
        #         max_stack.append(max(data))
        #     res.append(max_stack[0])
        # return res
        for i,j in enumerate(nums):
            print(i,j)

class Solution():
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        for i,j in enumerate(nums):
            while deque and deque[0] <= i-k: deque.popleft()
            while deque and j > nums[deque[-1]] : deque.pop()
            deque.append(i)
            if k - 1 <= i:
                res.append(nums[deque[0]])
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.maxSlidingWindow([1, 3, -1, -3, -1, 3, 6, 7], 3)
    print(res)