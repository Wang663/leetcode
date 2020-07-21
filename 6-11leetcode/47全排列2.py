# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
#  示例:
#
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums.sort()
        self.fun(nums,[])
        return self.res

    def fun(self, nums, last_res):
        if not nums:
            self.res.append(last_res)
            return
        self.fun(nums[0:0] + nums[1:], last_res+[nums[0]])
        for i in range(1, len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            self.fun(nums[0:i] + nums[i + 1:], last_res+[nums[i]])



# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         if not nums: return []
#         nums.sort()
#         res = []
#
#         def backtrack(nums, tmp):
#             if not nums:
#                 res.append(tmp)
#                 return
#             for i in range(len(nums)):
#                 if i > 0 and nums[i] == nums[i - 1]:
#                     continue
#                 backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
#
#         backtrack(nums, [])
#         return res



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.permuteUnique([1,2, 1])
    print(res)
