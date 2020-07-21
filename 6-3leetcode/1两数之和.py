# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_ = {}
        result = set()
        for i in range(len(nums)):
            dict_.setdefault(nums[i], []).append(i)
            if target - nums[i] == nums[i]:
                if len(dict_[nums[i]]) >= 2:
                    result.add(dict_[nums[i]].pop())
                    result.add(dict_[nums[i]].pop())
            else:
                if target - nums[i] in dict_.keys():
                    result.add(dict_[nums[i]][0])
                    result.add(dict_[target - nums[i]][0])
        print(dict_)
        return list(result)
        # for i in dict_.keys():
        #     if target-i ==i:
        #         if len(dict_[i])>=2:
        #             result.add(dict_[i][0])
        #             result.add(dict_[i][1])
        #             dict_[i].pop()
        #             dict_[i].pop()
        #     else:
        #         if target-i in dict_.keys():
        #             result.add(dict_[i][0])
        #             result.add(dict_[target-i][0])
        # print(dict_)
        # return list(result)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    solution = Solution()
    two_sum = solution.twoSum([1,0,1,0], 1)
    print(two_sum)
