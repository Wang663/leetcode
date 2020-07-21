# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
#  示例:
#
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        for i in range(len(nums)):
            self.fun(nums[0:i]+nums[i+1:],[nums[i]])
        return self.res

    def fun(self,nums,last_res):
        if not nums:
            self.res.append(last_res)
            return
        for i in range(len(nums)):
            self.fun(nums[0:i]+nums[i+1:],last_res+[nums[i]])

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    res = solution.permute([1, 2, 3,4])
    print(res)
    print(len(res))
