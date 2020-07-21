# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回
#  0。
#
#  示例:
#
#  输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
#
#
#  进阶:
#
#  如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#  Related Topics 数组 双指针 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if s > sum(nums):
            return 0
        i = 0
        j = 0
        sum_num = 0
        length = len(nums)
        res = length + 1
        while j < length:
            while j < length and sum_num < s:
                sum_num += nums[j]
                j += 1
            while sum_num >= s:
                res = min(j - i, res)
                sum_num -= nums[i]
                i += 1
        return res





# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(res)
